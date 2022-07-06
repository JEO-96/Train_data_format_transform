import os
import shutil
import random


def check_directory(dir_name):
    try:
        images_dir = os.path.join(dir_name, "images")
        labels_dir = os.path.join(dir_name, "labels")
        if not os.path.exists(images_dir):
            print(f'{images_dir} 디렉토리 생성')
            os.makedirs(images_dir)
        if not os.path.exists(labels_dir):
            print(f'{labels_dir} 디렉토리 생성')
            os.makedirs(labels_dir)
    except OSError:
        print(f'Error Creating directory. {dir_name}')


def split_data(path):
    txt_dir_path = os.path.join(path, 'labels')
    img_dir_path = os.path.join(path, 'images')
    txt_file_list = os.listdir(txt_dir_path)
    random.shuffle(txt_file_list)
    for txt in txt_file_list[0:1400]:
        img = txt.split('.')[0] + '.png'
        shutil.copy(os.path.join(img_dir_path, img), f'CARLA_1/images/{img}')
        shutil.copy(os.path.join(txt_dir_path, txt), f'CARLA_1/labels/{txt}')
        print(txt)
    for txt in txt_file_list[1400:2800]:
        img = txt.split('.')[0] + '.png'
        shutil.copy(os.path.join(img_dir_path, img), f'CARLA_2/images/{img}')
        shutil.copy(os.path.join(txt_dir_path, txt), f'CARLA_2/labels/{txt}')
        print(txt)
    for txt in txt_file_list[2800:4200]:
        img = txt.split('.')[0] + '.png'
        shutil.copy(os.path.join(img_dir_path, img), f'CARLA_3/images/{img}')
        shutil.copy(os.path.join(txt_dir_path, txt), f'CARLA_3/labels/{txt}')
        print(txt)
    for txt in txt_file_list[4200:5600]:
        img = txt.split('.')[0] + '.png'
        shutil.copy(os.path.join(img_dir_path, img), f'CARLA_4/images/{img}')
        shutil.copy(os.path.join(txt_dir_path, txt), f'CARLA_4/labels/{txt}')
        print(txt)
    for txt in txt_file_list[5600:7000]:
        img = txt.split('.')[0] + '.png'
        shutil.copy(os.path.join(img_dir_path, img), f'CARLA_5/images/{img}')
        shutil.copy(os.path.join(txt_dir_path, txt), f'CARLA_5/labels/{txt}')
        print(txt)
    for txt in txt_file_list[7000:8400]:
        img = txt.split('.')[0] + '.png'
        shutil.copy(os.path.join(img_dir_path, img), f'CARLA_6/images/{img}')
        shutil.copy(os.path.join(txt_dir_path, txt), f'CARLA_6/labels/{txt}')
        print(txt)


if __name__ == '__main__':
    check_directory("CARLA_1")
    check_directory("CARLA_2")
    check_directory("CARLA_3")
    check_directory("CARLA_4")
    check_directory("CARLA_5")
    check_directory("CARLA_6")
    split_data(r'//desktop-d8hc3hj/Server/Virtual_Data/CARLA_ClearNoon_All/train')
