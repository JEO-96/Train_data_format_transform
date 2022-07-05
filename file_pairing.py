import os


def pairing(img_dir_name, label_img_dir_name):
    img_dir_list = os.listdir(img_dir_name)
    label_img_dir_list = os.listdir(label_img_dir_name)
    for file in img_dir_list:
        if file not in label_img_dir_list:
            os.remove(os.path.join(img_dir_name, file))
            print(os.path.join(img_dir_name, file))


if __name__ == '__main__':
    pairing(r"D:\yolov5_modify\runs\detect\ClearNoonTown07\images", r"D:\yolov5_modify\runs\detect\ClearNoonTown07")
