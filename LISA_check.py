import json


def GetFilePath(path):
    lablepath = r"{}".format(path)
    return lablepath


def MakeEmptyFile(emptyFileName):
    pass


def MakeFile(file_name, Annotation_tag, left, top, right, bottom, over_count):
    file_name = file_name.split('/')[-1]
    file_name = file_name.split('.')[0]
    for i in file_name["annotation"]:
        left, top, right, bottom = i["bbox"]
        if left >= right or top >= bottom:
            input(f"에러발생 file name: {i['id']}, left: {left}, right: {right}, top: {top}, bottom: {bottom}")


def TransForm(labels):
    fr = open(labels, 'r')
    json_data = json.load(fr)
    for i in json_data["annotation"]:
        left, top, right, bottom = i["bbox"]
        print(i)
        if left >= right or top >= bottom:
            input(f"에러발생 file name: {i['id']}, left: {left}, right: {right}, top: {top}, bottom: {bottom}")

if __name__ == '__main__':
    TransForm(r'E:\instances_train2017.json')
