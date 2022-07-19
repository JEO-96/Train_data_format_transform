import json
import os
import shutil
from collections import deque


# import detectron2.structures import BoxMode
# AIHUB json 파일을 읽어서 detectron2 format으로 변형

def get_file_list(dir_path):
    file_list = os.listdir(dir_path)
    for f in range(len(file_list)):
        file_list[f] = os.path.join(dir_path, file_list[f])
    return file_list


def file_copy(dir_path, file_list):
    for f in file_list:
        file_name = f.split('\\')[-1].split('.')[0] + '.json'

        json_file = os.path.join(dir_path, file_name)
        print(json_file)
        shutil.copyfile(json_file, os.path.join('.', file_name))


def aihub2detectron(aihub_json_path):
    aihub_json_list = os.listdir(aihub_json_path)

    dataset_dicts = deque()
    for idx, v in enumerate(aihub_json_list):
        with open(os.path.join(aihub_json_path, v), 'r') as f:
            json_data = json.load(f)

        record = {}

        filename = os.path.join(aihub_json_path, json_data["image"]["filename"])
        width, height = json_data["image"]["imsize"]

        record["file_name"] = filename
        record["image_id"] = idx
        record["height"] = height
        record["width"] = width

        annos = json_data["annotation"]
        objs = deque()
        for anno in annos:
            if anno["class"] == "traffic_light":
                if anno["direction"] == "horizontal":
                    c_id = category_id(anno["attribute"][0])
                    if c_id:
                        obj = {
                            "bbox": [anno["box"][0], anno["box"][1], anno["box"][2], anno["box"][3]],
                            # "bbox_mode": BoxMode.XYXY_ABS,
                            "segmentation": [],
                            "category_id": c_id,
                        }
                        objs.append(obj)
                record["annotations"] = objs
                dataset_dicts.append(record)
            print(json.dumps(dataset_dicts, indent="\t"))
            with open('./test.json', 'w') as make_file:
                json.dump(dataset_dicts, make_file, indent="\t")
    return dataset_dicts


def category_id(attribute):
    if attribute["red"] == "on" and attribute["green"] == "off" and attribute["x_light"] == "off" and \
            attribute["others_arrow"] == "off" and attribute["yellow"] == "off" and attribute["left_arrow"] == "off":
        c_id = 0
    elif attribute["red"] == "off" and attribute["green"] == "off" and attribute["x_light"] == "off" and \
            attribute["others_arrow"] == "off" and attribute["yellow"] == "on" and attribute["left_arrow"] == "off":
        c_id = 1
    elif attribute["red"] == "off" and attribute["green"] == "on" and attribute["x_light"] == "off" and \
            attribute["others_arrow"] == "off" and attribute["yellow"] == "off" and attribute["left_arrow"] == "off":
        c_id = 2
    elif attribute["red"] == "off" and attribute["green"] == "on" and attribute["x_light"] == "off" and \
            attribute["others_arrow"] == "off" and attribute["yellow"] == "off" and attribute["left_arrow"] == "on":
        c_id = 3
    elif attribute["red"] == "on" and attribute["green"] == "off" and attribute["x_light"] == "off" and \
            attribute["others_arrow"] == "off" and attribute["yellow"] == "off" and attribute["left_arrow"] == "on":
        c_id = 4
    else:
        c_id = None
    return c_id


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flie_list = get_file_list(r"D:\AIHUB5_extract\val\labels")
    file_copy(r"G:\py_json\val", flie_list)
    # dataset_dicts = aihub2detectron(r"C:\Users\user\Desktop\AIHUB5_extract\jsons")
