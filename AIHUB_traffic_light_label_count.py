import os
import json
import collections
import re
import shutil

# AIHUB의 교통신호/표지판 json 파일을 읽어서 클래스 파일 개수가 몇개인지 세는 프로그램
count = collections.defaultdict(int)


def classify(path):
    file_list = os.listdir(path)
    file_list_json = [file for file in file_list if file.endswith('.json')]

    for f_json in file_list_json:
        json_file_name = path + '/' + f_json
        jpg_file_name = path + '/' + f_json.split('.')[0] + '.jpg'
        print(json_file_name)
        with open(json_file_name, "r") as st_json:
            st_python = json.load(st_json)
            for a in st_python['annotation']:
                if a['class'] == 'traffic_light' and a['direction'] == 'horizontal' and a['type'] == 'car':
                    #    and (a['light_count'] == '3' or a['light_count'] == '4'):
                    count[str(a['attribute'][0])] += 1
                    check_directory(str(a['attribute'][0]))
                    # shutil.copy(jpg_file_name, re.sub('[^a-z0-9]', ' ', str(a['attribute'][0]))[:-2] + '/' + f_json.split('.')[0] + '.jpg')
        print(count)


def check_directory(class_name):
    class_name = re.sub('[^a-z0-9]', ' ', class_name)
    try:
        if not os.path.exists(class_name):
            print('class_name:', class_name)
            os.makedirs(class_name)
    except OSError:
        print('Error: Creating directory. ' + class_name)


if __name__ == '__main__':
    classify(r'G:\TrafficLight\Training')
    # classify(r'G:\AIHUB5_extract\val\json')
