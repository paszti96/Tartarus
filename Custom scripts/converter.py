import json
import cv2

file_name = r"D:\Tartarus\Data\test\dataset\captures_000.json"
folder = r".\test\test_images1"
depth_folder = r".\test\depth"

img_w = 1263
img_h = 947
file = open(file_name)
annotations = json.load(file)

for capture in annotations["captures"]:
    # print(json.dumps(capture, indent=3))
    name = capture["filename"].split(r"/")[-1].split(".")[0]
    bb2dlabels = capture["annotations"][0]["values"]
    instance_segmentation_labels = capture["annotations"][0]["values"]
    bb3dlabels = capture["annotations"][2]["values"]
    # annotation_file = open(folder + "\\" + name + ".txt", "w")
    # todo: test
    depth_im = cv2.imread(depth_folder + "\\" + name.split("_")[-1] + ".png")
    gray = cv2.cvtColor(depth_im, cv2.COLOR_BGR2GRAY)
    rgb_im = cv2.imread(folder + "\\" + name + ".png")
    # todo: add another chanell

    print(folder + "\\" + name + ".txt")
    for label in bb2dlabels:
        x = label["x"]
        y = label["y"]
        w = label["width"]
        h = label["height"]
        # annotation_file.write(
        #     "{} {} {} {} {}\n".format(label["label_id"]-1,
        #                               (x+w//2)/img_w,
        #                               (y+h//2)/img_h,
        #                               w/img_w,
        #                               h/img_h
        #                               )
        # )

        print(
            label["label_id"]-1,
            (x+w//2)/img_w,
            (y+h//2)/img_h,
            w/img_w,
            h/img_h
        )

    # annotation_file.close()

print("done")
