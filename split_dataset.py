"""
데이터셋을 랜덤으로 순서를 섞은후 파일을 나누는 기능
"""
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
    for i, txt in enumerate(txt_file_list[0:7000]):
        img = txt.split('.')[0] + '.png'
        shutil.copy(os.path.join(img_dir_path, img), f'CARLA_3_/images/{img}')
        shutil.copy(os.path.join(txt_dir_path, txt), f'CARLA_3_/labels/{txt}')
        print(txt, i)
    # for txt in txt_file_list[1400:2800]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_02/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_02/labels/{txt}')
    #     print(txt)
    # for txt in txt_file_list[2800:4200]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_03/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_03/labels/{txt}')
    #     print(txt)
    # for txt in txt_file_list[4200:5600]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_04/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_04/labels/{txt}')
    #     print(txt)
    # for txt in txt_file_list[5600:7000]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_05/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_05/labels/{txt}')
    #     print(txt)
    # for txt in txt_file_list[7000:8400]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_06/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_06/labels/{txt}')
    #     print(txt)
    # for txt in txt_file_list[8400:9800]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_07/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_07/labels/{txt}')
    #     print(txt)
    # for txt in txt_file_list[9800:11200]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_08/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_08/labels/{txt}')
    #     print(txt)
    # for txt in txt_file_list[11200:12600]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_09/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_09/labels/{txt}')
    #     print(txt)
    # for txt in txt_file_list[12600:]:
    #     img = txt.split('.')[0] + '.jpg'
    #     shutil.copy(os.path.join(img_dir_path, img), f'LISA_10/images/{img}')
    #     shutil.copy(os.path.join(txt_dir_path, txt), f'LISA_10/labels/{txt}')
    #     print(txt)


if __name__ == '__main__':
    # check_directory("LISA_3_")
    check_directory("CARLA_3_")
    # check_directory("LISA_03")
    # check_directory("LISA_04")
    # check_directory("LISA_05")
    # check_directory("LISA_06")
    # check_directory("LISA_07")
    # check_directory("LISA_08")
    # check_directory("LISA_09")
    # check_directory("LISA_10")
    split_data(r'\\DESKTOP-D8HC3HJ\Server\주은오\CARLA_3')
