import os
import cv2


def GetFilePath(path):
    imagepath = r"{}".format(path)
    imagepaths = [os.path.join(imagepath, name) for name in os.listdir(imagepath)]
    return imagepaths


def BGR2HSV(images):
    print(images[0])
    folder_name = images[0].split('/')[-1].split('\\')[0]
    super_folder_name = images[0].split('/')[-2]

    try:
        if not os.path.exists(super_folder_name):
            os.makedirs(super_folder_name)
        if not os.path.exists(super_folder_name + '/' + folder_name):
            os.makedirs(super_folder_name + '/' + folder_name)
    except OSError:
        print('Error: Creating directory. ' + folder_name)

    for L in range(len(images)):
        img = cv2.imread(images[L])
        HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        HSV = cv2.cvtColor(HSV, cv2.COLOR_RGB2BGR)
        file_name = images[L].split('\\')[-1]
        cv2.imwrite(f'{super_folder_name}/{folder_name}/{file_name}', HSV)
        print(f'{super_folder_name}/{folder_name}/{file_name}')


def clahe(images):
    print(images[0])
    folder_name = images[0].split('/')[-1].split('\\')[0]
    super_folder_name = images[0].split('/')[-2]

    try:
        if not os.path.exists(super_folder_name):
            os.makedirs(super_folder_name)
        if not os.path.exists(super_folder_name + '/' + folder_name):
            os.makedirs(super_folder_name + '/' + folder_name)
    except OSError:
        print('Error: Creating directory. ' + folder_name)

    for L in range(len(images)):
        img = cv2.imread(images[L])
        yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        yuv[:, :, 0] = clahe.apply(yuv[:, :, 0])
        yuv = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        file_name = images[L].split('\\')[-1]
        cv2.imwrite(f'{super_folder_name}/{folder_name}/{file_name}', yuv)
        print(f'{folder_name}/{file_name}')


def he(images):
    print(images[0])
    folder_name = images[0].split('/')[-1].split('\\')[0]
    super_folder_name = images[0].split('/')[-2]

    try:
        if not os.path.exists(super_folder_name):
            os.makedirs(super_folder_name)
        if not os.path.exists(super_folder_name + '/' + folder_name):
            os.makedirs(super_folder_name + '/' + folder_name)
    except OSError:
        print('Error: Creating directory. ' + folder_name)

    for L in range(len(images)):
        img = cv2.imread(images[L])
        yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
        yuv = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        file_name = images[L].split('\\')[-1]
        cv2.imwrite(f'{super_folder_name}/{folder_name}/{file_name}', yuv)
        print(f'{folder_name}/{file_name}')


if __name__ == '__main__':
    images = GetFilePath('C:/Users/user/Desktop/archive/day/train/images')
    clahe(images)
    images = GetFilePath('C:/Users/user/Desktop/archive/day/val/images')
    clahe(images)
