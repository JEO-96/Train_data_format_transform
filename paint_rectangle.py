import os
import cv2


def paint_rectangle(img_path, txt_path):
    txt_file_list = os.listdir(txt_path)
    image_file_list = os.listdir(img_path)

    for i in range(len(txt_file_list)):
        img = cv2.imread(os.path.join(img_path, image_file_list[i]))
        txt = open(os.path.join(txt_path, txt_file_list[i]), 'r')
        height, width, channel = img.shape
        for line in txt.readlines():
            _, x, y, w, h = map(float, line.split())
            left = int((x - (w / 2)) * width)
            right = int((x + (w / 2)) * width)
            top = int((y - (h / 2)) * height)
            bottom = int((y + (h / 2)) * height)
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 3)
        cv2.imwrite(f"labeled_image/{image_file_list[i]}", img)


def check_directory():
    try:
        images_dir = "labeled_image"
        if not os.path.exists(images_dir):
            print(f'{images_dir} 디렉토리 생성')
            os.makedirs(images_dir)
    except OSError:
        print(f'Error Creating directory.')


if __name__ == '__main__':
    check_directory()
    paint_rectangle(r"C:\Users\user\Desktop\archive\day\train\images",
                    r"C:\Users\user\Desktop\archive\day\train\labels")
