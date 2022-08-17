import os


def pairing(img_dir_name, label_img_dir_name):
    img_dir_list = os.listdir(img_dir_name)
    label_img_dir_list = os.listdir(label_img_dir_name)
    for file in img_dir_list:
        if file not in label_img_dir_list:
            os.remove(os.path.join(img_dir_name, file))
            print(os.path.join(img_dir_name, file))


if __name__ == '__main__':
<<<<<<< HEAD
    pairing(r"\\DESKTOP-D8HC3HJ\Server\Virtual_Data\CARLA_ClearNoon_2\ClearNoonTown10\images", r"\\DESKTOP-D8HC3HJ\Server\Virtual_Data\CARLA_ClearNoon_2\ClearNoonTown10")
=======
    pairing(r"\\DESKTOP-D8HC3HJ\Server\Virtual_Data\CARLA_ClearNoon_3\exp7\images",
            r"\\DESKTOP-D8HC3HJ\Server\Virtual_Data\CARLA_ClearNoon_3\exp7")
>>>>>>> b04539fd67a8c97c261df0528c1e471c010fd26b
