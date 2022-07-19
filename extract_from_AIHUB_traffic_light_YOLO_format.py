import os
import pandas as pd
import random
import shutil
from collections import defaultdict

# 원본파일에서 랜덤으로 10분의 1만 복사하는 프로그램

def search(dirname):
    images = os.path.join(dirname, "images")
    labels = os.path.join(dirname, "labels")

    if not os.path.isdir('images'):
        os.makedirs('images')
    if not os.path.isdir('labels'):
        os.makedirs('labels')
    img_list = []
    label_list = []
    # 이미지와 레이블 list로 저장
    for image in os.listdir(images):
        img_list.append(os.path.join(images, image))
    for label in os.listdir(labels):
        label_list.append(os.path.join(labels, label))

    extract(img_list, label_list)


def extract(img_list, label_list):
    if len(img_list) == len(label_list):
        list = []
        ran_num = random.randint(0, len(img_list))
        for i in range(int(len(img_list) / 10)):
            while ran_num in list:
                ran_num = random.randint(0, len(img_list))
            list.append(ran_num)

        for i in list:
            shutil.copy2(img_list[i], os.path.join(img_list[i].split("\\")[-2], img_list[i].split("\\")[-1]))
            shutil.copy2(label_list[i], os.path.join(label_list[i].split("\\")[-2], label_list[i].split("\\")[-1]))
            print(img_list[i])

def label_count(path):
    count = defaultdict(int)
    for label in os.listdir(path):
        label = os.path.join(path, label)
        f = open(label, 'r')
        while True:
            line = f.readline()
            if not line: break
            cls = line.split()[0]
            count[cls] += 1
            print(count)
        f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    search(r'D:\AIHUB_c5\val')
    # label_count(r'.\labels')