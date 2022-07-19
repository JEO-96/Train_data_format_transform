import json
import shutil
import os


# 신호등과 표지판 파일에서 신호등 파일만 걸러낸것


def check_directory():
    try:
        if not os.path.exists('images'):
            os.makedirs('images')
    except OSError:
        print('Error: Creating directory. ' + 'images')
    try:
        if not os.path.exists('jsons'):
            os.makedirs('jsons')
    except OSError:
        print('Error: Creating directory. ' + 'labels')


def get_file_name(path):
    file_list = os.listdir(path)
    file_list_json = [file for file in file_list if file.endswith('.json')]

    for f_json in file_list_json:
        json_file_name = path + '/' + f_json
        print(json_file_name)
        jpg_file_name = path + '/' + f_json.split('.')[0] + '.jpg'
        print(jpg_file_name)
        with open(json_file_name, "r") as st_json:
            st_python = json.load(st_json)
            for a in st_python['annotation']:
                if a['class'] == 'traffic_light' and a['direction'] == 'horizontal' and a['type'] == 'car' \
                        and (a['light_count'] == '3' or a['light_count'] == '4'):
                    # print(st_python['annotation'])
                    print(a['light_count'])
                    print(a['attribute'])

                    shutil.copy(json_file_name, 'jsons/' + f_json)
                    shutil.copy(jpg_file_name, 'images/' + f_json.split('.')[0] + '.jpg')
                    break


if __name__ == '__main__':
    check_directory()
    get_file_name("G:/TrafficLight/Training")
