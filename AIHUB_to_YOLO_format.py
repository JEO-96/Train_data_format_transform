import os
import json


def check_directory():
    try:
        if not os.path.exists('train/labels'):
            os.makedirs('train/labels')
    except OSError:
        print('Error: Creating directory. ' + 'train/labels')
    try:
        if not os.path.exists('val/labels'):
            os.makedirs('val/labels')
    except OSError:
        print('Error: Creating directory. ' + 'val/labels')
    try:
        if not os.path.exists('test/labels'):
            os.makedirs('test/labels')
    except OSError:
        print('Error: Creating directory. ' + 'test/labels')


def train_trans_form(path):
    file_list = os.listdir(path)
    file_list_json = [file for file in file_list if file.endswith('.json')]

    for f_json in file_list_json:
        json_file_name = path + '/' + f_json
        with open(json_file_name, "r") as st_json:
            st_python = json.load(st_json)
            img_weight, img_height = st_python['image']['imsize']
            data = ""
            for a in st_python['annotation']:
                f = f_json.split('.')[0]
                fw = open("train/labels/{}.txt".format(f), 'w')

                if a['class'] == 'traffic_light' and a['direction'] == 'horizontal' and a['type'] == 'car' \
                        and (a['light_count'] == '3' or a['light_count'] == '4'):
                    left, top, right, bottom = a['box']
                    print(f_json)
                    x = (left + right) / 2 / img_weight
                    y = (top + bottom) / 2 / img_height
                    w = abs((right - left) / img_weight)
                    h = abs((bottom - top) / img_height)
                    if len(a['attribute']) > 1:
                        input('ERROR:attribute len > 2')
                    Class_ID = class_id(a)
                    if Class_ID is not None:
                        data += f'{Class_ID} {x} {y} {w} {h}\n'
            print(data)
            fw.write(data)
            fw.close()


def val_trans_form(path):
    file_list = os.listdir(path)
    file_list_json = [file for file in file_list if file.endswith('.json')]

    for f_json in file_list_json:
        json_file_name = path + '/' + f_json
        with open(json_file_name, "r") as st_json:
            st_python = json.load(st_json)
            img_weight, img_height = st_python['image']['imsize']
            data = ""
            for a in st_python['annotation']:
                f = f_json.split('.')[0]
                fw = open("val/labels/{}.txt".format(f), 'w')

                if a['class'] == 'traffic_light' and a['direction'] == 'horizontal' and a['type'] == 'car' \
                        and (a['light_count'] == '3' or a['light_count'] == '4'):
                    left, top, right, bottom = a['box']
                    print(f_json)
                    x = (left + right) / 2 / img_weight
                    y = (top + bottom) / 2 / img_height
                    w = abs((right - left) / img_weight)
                    h = abs((bottom - top) / img_height)
                    if len(a['attribute']) > 1:
                        input('ERROR:attribute len > 2')
                    Class_ID = class_id(a)
                    if Class_ID is not None:
                        data += f'{Class_ID} {x} {y} {w} {h}\n'
            print(data)
            fw.write(data)
            fw.close()

def test_trans_form(path):
    file_list = os.listdir(path)
    file_list_json = [file for file in file_list if file.endswith('.json')]

    for f_json in file_list_json:
        json_file_name = path + '/' + f_json
        with open(json_file_name, "r") as st_json:
            st_python = json.load(st_json)
            img_weight, img_height = st_python['image']['imsize']
            data = ""
            for a in st_python['annotation']:
                f = f_json.split('.')[0]
                fw = open("test/labels/{}.txt".format(f), 'w')

                if a['class'] == 'traffic_light' and a['direction'] == 'horizontal' and a['type'] == 'car' \
                        and (a['light_count'] == '3' or a['light_count'] == '4'):
                    left, top, right, bottom = a['box']
                    print(f_json)
                    x = (left + right) / 2 / img_weight
                    y = (top + bottom) / 2 / img_height
                    w = abs((right - left) / img_weight)
                    h = abs((bottom - top) / img_height)
                    if len(a['attribute']) > 1:
                        input('ERROR:attribute len > 2')
                    Class_ID = class_id(a)
                    if Class_ID is not None:
                        data += f'{Class_ID} {x} {y} {w} {h}\n'
            print(data)
            fw.write(data)
            fw.close()

def class_id(annotation):
    attribute = annotation['attribute'][0]
    # 3_정지
    if annotation['light_count'] == '3' and attribute['red'] == 'on' and attribute['yellow'] == 'off' \
            and attribute['green'] == 'off' and attribute['x_light'] == 'off' and attribute['others_arrow'] == 'off' \
            and attribute['left_arrow'] == 'off':
        return '0'
    # 3_경고
    elif annotation['light_count'] == '3' and attribute['red'] == 'off' and attribute['yellow'] == 'on' \
            and attribute['green'] == 'off' and attribute['x_light'] == 'off' and attribute['others_arrow'] == 'off' \
            and attribute['left_arrow'] == 'off':
        return '1'
    # 3_전진
    elif annotation['light_count'] == '3' and attribute['red'] == 'off' and attribute['yellow'] == 'off' \
            and attribute['green'] == 'on' and attribute['x_light'] == 'off' and attribute['others_arrow'] == 'off' \
            and attribute['left_arrow'] == 'off':
        return '2'
    # 4색 정지
    elif annotation['light_count'] == '4' and attribute['red'] == 'on' and attribute['yellow'] == 'off' \
            and attribute['green'] == 'off' and attribute['x_light'] == 'off' and attribute['others_arrow'] == 'off' \
            and attribute['left_arrow'] == 'off':
        return '3'
    # 4색 경고
    elif annotation['light_count'] == '4' and attribute['red'] == 'off' and attribute['yellow'] == 'on' \
            and attribute['green'] == 'off' and attribute['x_light'] == 'off' and attribute['others_arrow'] == 'off' \
            and attribute['left_arrow'] == 'off':
        return '4'
    # 4색 직진
    elif annotation['light_count'] == '4' and attribute['red'] == 'off' and attribute['yellow'] == 'off' \
            and attribute['green'] == 'on' and attribute['x_light'] == 'off' and attribute['others_arrow'] == 'off' \
            and attribute['left_arrow'] == 'off':
        return '5'
    # 직좌
    elif annotation['light_count'] == '4' and attribute['red'] == 'off' and attribute['yellow'] == 'off' \
            and attribute['green'] == 'on' and attribute['x_light'] == 'off' and attribute['others_arrow'] == 'off' \
            and attribute['left_arrow'] == 'on':
        return '6'
    # 좌회전
    elif annotation['light_count'] == '4' and attribute['red'] == 'on' and attribute['yellow'] == 'off' \
            and attribute['green'] == 'off' and attribute['x_light'] == 'off' and attribute['others_arrow'] == 'off' \
            and attribute['left_arrow'] == 'on':
        return '7'
    else:
        return None


if __name__ == '__main__':
    check_directory()
    train_trans_form(r'G:\AIHUB8_extract\train\jsons')
    val_trans_form(r'G:\AIHUB8_extract\val\json')
    # test_trans_form(r'G:\py_json\test\jsons')