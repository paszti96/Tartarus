import json, cv2, os, glob
import numpy as np

class Rect:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2          #x+w
        self.y2 = y2          #y+h

    @staticmethod
    def intersection(one, other):
        # gives bottom-left point
        # of intersection rectangle
        x5 = int(max(one.x1, other.x1))
        y5 = int(max(one.y1, other.y1))

        # gives top-right point
        # of intersection rectangle
        x6 = int(min(one.x2, other.x2))
        y6 = int(min(one.y2, other.y2))

        # no intersection
        if (x5 > x6 or y5 > y6):
            # print("No intersection")
            return None

        return Rect(x5,y5,x6,y6)

def preprocess(dataset):
    #file_name = fr"C:\Users\paszti\Documents\Tartarus_hdr\Data\{dataset}\dataset\captures_000.json"

    folder = fr".\{dataset}\images{dataset}"
    depth_folder = fr".\{dataset}\depth"
    output_folder = fr"D:\RODSIE_yolov5\data\{dataset}"

    img_w = 1263
    img_h = 947

    file_names = fr"D:/Tartarus/Data/{dataset}/dataset/captures_*"
    for file_name in glob.glob(file_names):
        print(file_name)
        file = open(file_name)
        annotations = json.load(file)

        instance_data_dict = {}

        """Extract data from annotation file"""
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        # annotation_file = open(output_folder+"\\train.txt", "w")

        for capture in annotations["captures"]:
            # print(json.dumps(capture, indent=3))

            name = capture["filename"].split(r"/")[-1].split(".")[0]
            bb2dlabels = capture["annotations"][0]["values"]
            instance_segmentation_labels = capture["annotations"][0]["values"]
            bb3dlabels = capture["annotations"][2]["values"]
            annotation_file = open( output_folder + "\\" + name + ".txt", "w")


            """Combining depth and rgb image"""
            depth_im = cv2.imread(depth_folder + "\\" +"Main Camera_depth_" + str(int(name.split("_")[-1])-1) + ".png")
            if depth_im is not None:
                d = cv2.cvtColor(depth_im, cv2.COLOR_BGR2GRAY)
            else:
                d = np.full((rgb_im.shape[0], rgb_im.shape[1], 1), 255, dtype="uint8")
            img_name2save = "\\" + name + ".png"
            rgb_im = cv2.imread(folder + img_name2save)
            r, g, b = cv2.split(rgb_im)
            input = cv2.merge((r, g, b, d))
            image_path = output_folder + img_name2save
            cv2.imwrite(image_path,input)
            print(image_path)

            """Creating .txt file 4 training"""
            line = image_path
            for label in bb2dlabels:
                x = label["x"]
                y = label["y"]
                w = label["width"]
                h = label["height"]
                id = label["label_id"]

                """Saving data into a file"""
                annotation_file.write( "{} {} {} {} {}\n".format(id - 1,
                                          (x + w // 2) / img_w,
                                          (y + h // 2) / img_h,
                                          w / img_w,
                                          h / img_h
                                          )
                                      )
                # line += " {},{},{},{},{}".format(
                #                               x,
                #                               y,
                #                               x+w,
                #                               y+h,
                #                               id - 1
                #                               )

                # print(
                #     id-1,
                #     (x+w//2)/img_w,
                #     (y+h//2)/img_h,
                #     w/img_w,
                #     h/img_h
                # )
                instance_data_dict[label["instance_id"]] = label
            annotation_file.close()


            """creating mask for intersections"""
            mask_img = np.zeros((rgb_im.shape[0], rgb_im.shape[1], 1), dtype="uint8")
            for item in instance_data_dict:

                    if 'bb_intersections' in instance_data_dict[item]:
                        for hidden_obj in instance_data_dict[item]['bb_intersections']:
                            r1 = Rect(
                                instance_data_dict[item]['x'],
                                instance_data_dict[item]['y'],
                                instance_data_dict[item]['x'] + instance_data_dict[item]['width'],
                                instance_data_dict[item]['y'] + instance_data_dict[item]['height']
                            )
                            r2 = Rect(
                                instance_data_dict[hidden_obj]['x'],
                                instance_data_dict[hidden_obj]['y'],
                                instance_data_dict[hidden_obj]['x'] + instance_data_dict[hidden_obj]['width'],
                                instance_data_dict[hidden_obj]['y'] + instance_data_dict[hidden_obj]['height']
                            )
                            r3 = Rect.intersection(r1,r2)
                            if r3 is not None:
                                p1 = (r3.x1,r3.y1)
                                p2 =(r3.x2,r3.y2)
                                mask_img = cv2.rectangle(mask_img,pt1=p1,pt2=p2,color=255,thickness=-1)
                            instance_data_dict[hidden_obj]['x']  < instance_data_dict[item]['x']
                    else:
                        print("Wrong dataset. Please generate new dataset with custom script.")
                        break

            # cv2.imshow('hey', mask_img)
            # cv2.waitKey()
            #print(output_folder + "\\mask" + name + ".png")
            mask_img = cv2.cvtColor(mask_img,cv2.COLOR_RGB2RGBA)
            cv2.imwrite(output_folder + "\\mask_" + name.split("_")[-1] + ".png",mask_img)

    print(f"done {dataset}")

if __name__ == '__main__':
    datasets = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]

    for dataset in datasets:
        preprocess(dataset)