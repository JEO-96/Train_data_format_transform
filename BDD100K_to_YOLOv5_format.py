import json
import os
import cv2


def check_directory(class_name):
    try:
        if not os.path.exists(class_name):
            print('class_name:', class_name)
            os.makedirs(class_name)
    except OSError:
        print('Error: Creating directory. ' + class_name)


def train_trans_form(images_path, file):
    with open(file, 'r') as f:
        data_list = json.load(f)

    for data in data_list:
        fw = open(f"labels/{data['name'].split('.')[0]}.txt", 'w')
        content = ''
        for label in data["labels"]:

            if label["category"] == "traffic light":
                img = cv2.imread(os.path.join(images_path, data["name"]))
                img_height, img_width, channel = img.shape
                left = label["box2d"]["x1"]
                top = label["box2d"]["y1"]
                right = label["box2d"]["x2"]
                bottom = label["box2d"]["y2"]

                x = (left + right) / 2 / img_width
                y = (top + bottom) / 2 / img_height
                w = abs((right - left) / img_width)
                h = abs((bottom - top) / img_height)
                Class_ID = 0
                content += f'{Class_ID} {x} {y} {w} {h}\n'
                img.close
        print(content)
        fw.write(content)
        fw.close()


if __name__ == '__main__':
    check_directory("labels")
    train_trans_form(r"C:\Users\user\Desktop\bdd100k\images\100k\val",
                     r"C:\Users\user\Desktop\bdd100k\labels\bdd100k_labels_images_val.json")
