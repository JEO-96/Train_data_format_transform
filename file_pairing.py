"""
이미지와 레이블 파일을 확인하고 레이블이 존재하지 않는 이미지를 제거하는 프로그램
"""
import os


def pairing(img_dir_name, label_img_dir_name):
    img_dir_list = os.listdir(img_dir_name)
    label_img_dir_list = os.listdir(label_img_dir_name)
    for file in img_dir_list:
        if file not in label_img_dir_list:
            os.remove(os.path.join(img_dir_name, file))
            print(os.path.join(img_dir_name, file))


if __name__ == '__main__':
    pairing(r"D:\yolov5_modify\runs\detect\CARLA_LISA_3\images",
            r"D:\yolov5_modify\runs\detect\CARLA_LISA_3")

