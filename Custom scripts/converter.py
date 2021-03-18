import json
import cv2

file_name = r"C:\Users\paszti\Documents\Tartarus_hdr\Data\1\dataset\captures_000.json"
#file_name = r"D:\Tartarus\Data\test\dataset\captures_000.json"
folder = r".\1\images1"
depth_folder = r".\1\depth"
output_folder = r".\1\out"

img_w = 1263
img_h = 947
file = open(file_name)
annotations = json.load(file)

instance_data_dict = {}

"""Extract data from annotation file"""
for capture in annotations["captures"]:
    # print(json.dumps(capture, indent=3))
    name = capture["filename"].split(r"/")[-1].split(".")[0]
    bb2dlabels = capture["annotations"][0]["values"]
    instance_segmentation_labels = capture["annotations"][0]["values"]
    bb3dlabels = capture["annotations"][2]["values"]
    # annotation_file = open(folder + "\\" + name + ".txt", "w")
    # todo: test

    """Combining depth and rgb image"""
    depth_im = cv2.imread(depth_folder + "\\" +"Main Camera_depth_" + str(int(name.split("_")[-1])-2) + ".png")
    d = cv2.cvtColor(depth_im, cv2.COLOR_BGR2GRAY)
    img_name2save = "\\" + name + ".png"
    rgb_im = cv2.imread(folder + img_name2save)
    r,g,b = cv2.split(rgb_im)
    input = cv2.merge((r,g,b,d))

    #cv2.imwrite(output_folder + img_name2save,input)
    print(output_folder + "\\" + img_name2save)

    """Creating .txt file 4 training"""
    for label in bb2dlabels:
        x = label["x"]
        y = label["y"]
        w = label["width"]
        h = label["height"]
        id = label["label_id"]
        """Saving data into a file"""
        # annotation_file.write(
        #     "{} {} {} {} {}\n".format(id-1,
        #                               (x+w//2)/img_w,
        #                               (y+h//2)/img_h,
        #                               w/img_w,
        #                               h/img_h
        #                               )
        # )
        print(
            id-1,
            (x+w//2)/img_w,
            (y+h//2)/img_h,
            w/img_w,
            h/img_h
        )
        instance_data_dict[label["instance_id"]] = label
    # annotation_file.close()

    """creating mask for intersections"""
    for item in instance_data_dict:

            if 'bb_intersections' in instance_data_dict[item]:
                for hidden_obj in instance_data_dict[item]['bb_intersections']:
                    #todo: calculate intersection
                    instance_data_dict[hidden_obj]['x']  < instance_data_dict[item]['x']
            else:
                print("Wrong dataset. Please generate new dataset with custom script.")
                break


print("done")
