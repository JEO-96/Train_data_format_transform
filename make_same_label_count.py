"""
데이터 개수가 가장 작은 4구 노란불 신호등의 갯수 만큼 다른 신호등을 추출하는 프로그램
"""
import os
import shutil
import random

class_count = [0, 0, 0, 0, 0, 0, 0, 0]


def check_directory(dir_name):
    try:
        if not os.path.exists(dir_name):
            print(f'{dir_name} 디렉토리 생성')
            os.makedirs(dir_name)
    except OSError:
        print(f'Error Creating directory. {dir_name}')


def extract_4_warning(path):
    txt_dir_path = os.path.join(path, 'labels')
    img_dir_path = os.path.join(path, 'images')
    txt_file_list = os.listdir(txt_dir_path)
    global class_count
    for txt in txt_file_list:
        f = open(os.path.join(txt_dir_path, txt), 'r')
        lines = f.readlines()
        class_count_in_txt = [0, 0, 0, 0, 0, 0, 0, 0]
        for line in lines:
            c = int(line.split()[0])
            class_count_in_txt[c] += 1
        before_class_count = [class_count[0] + class_count_in_txt[0],
                              class_count[1] + class_count_in_txt[1],
                              class_count[2] + class_count_in_txt[2],
                              class_count[3] + class_count_in_txt[3],
                              class_count[4] + class_count_in_txt[4],
                              class_count[5] + class_count_in_txt[5],
                              class_count[6] + class_count_in_txt[6],
                              class_count[7] + class_count_in_txt[7]]
        if class_count_in_txt[4] != 0:
            class_count = before_class_count
            print(f'class_count: {class_count}')
            img = txt.split('.')[0] + '.jpg'
            # shutil.copy(os.path.join(img_dir_path, img), f'images/{img}')
            # shutil.copy(os.path.join(txt_dir_path, txt), f'labels/{txt}')
            print(txt)


def extract_data_len_minimum_class(path):
    txt_dir_path = os.path.join(path, 'labels')
    img_dir_path = os.path.join(path, 'images')
    txt_file_list = os.listdir(txt_dir_path)
    random.shuffle(txt_file_list)
    global class_count
    for txt in txt_file_list:
        f = open(os.path.join(txt_dir_path, txt), 'r')
        lines = f.readlines()
        class_count_in_txt = [0, 0, 0, 0, 0, 0, 0, 0]
        for line in lines:
            c = int(line.split()[0])
            class_count_in_txt[c] += 1
        before_class_count = [class_count[0] + class_count_in_txt[0],
                              class_count[1] + class_count_in_txt[1],
                              class_count[2] + class_count_in_txt[2],
                              class_count[3] + class_count_in_txt[3],
                              class_count[4] + class_count_in_txt[4],
                              class_count[5] + class_count_in_txt[5],
                              class_count[6] + class_count_in_txt[6],
                              class_count[7] + class_count_in_txt[7]]
        check = False
        for i in before_class_count:
            if i > before_class_count[4] or class_count_in_txt[4] > 0:
                check = True
                break
        if check:
            continue
        class_count = before_class_count
        print(f'class_count: {class_count}')
        img = txt.split('.')[0] + '.jpg'
        # shutil.copy(os.path.join(img_dir_path, img), f'images/{img}')
        # shutil.copy(os.path.join(txt_dir_path, txt), f'labels/{txt}')
        print(txt)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_directory("images")
    check_directory("labels")
    extract_4_warning(r'G:\AIHUB_c8\train')
    # extract_data_len_minimum_class(r'G:\AIHUB_c8\train')
