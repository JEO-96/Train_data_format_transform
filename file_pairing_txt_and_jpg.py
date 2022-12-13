import os


def pairing(img_dir_name, label_dir_name):
    img_dir_list = os.listdir(img_dir_name)
    label_dir_list = os.listdir(label_dir_name)
    for file in img_dir_list:
        file = file.split(".")[0] + ".txt"
        if file not in label_dir_list:
            file = file.split(".")[0] + ".jpg"
            os.remove(os.path.join(img_dir_name, file))
            print(os.path.join(img_dir_name, file))


if __name__ == '__main__':
    pairing(r"C:\Users\user\Desktop\bdd100k\images\100k\train",
            r"C:\Users\user\Desktop\bdd100k\train\labels")

