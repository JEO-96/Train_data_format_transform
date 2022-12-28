"""
YOLO format으로 변환한 AIHUB 교통신호/표지판 데이터셋에서 class 별 개수를 세는 프로그램
"""

import os


ID0 = 0
ID1 = 0
ID2 = 0
ID3 = 0
ID4 = 0
ID5 = 0
ID6 = 0
empty = 0


def get_file_path(path):
    label_path = r"{}".format(path)
    label_paths = [os.path.join(label_path, name) for name in os.listdir(label_path)]
    print(len(label_path), len(label_paths))
    return label_paths


def copy_file(labels):
    global ID0, ID1, ID2, ID3, ID4, ID5, ID6, empty
    fr = open(labels, 'r')
    while True:
        line = fr.readline()
        if not line: break
        if line.split()[0] != None:
            Class_ID = int(line.split()[0])
            if Class_ID == 0:
                ID0 += 1
            elif Class_ID == 1:
                ID1 += 1
            elif Class_ID == 2:
                ID2 += 1
            elif Class_ID == 3:
                ID3 += 1
            elif Class_ID == 4:
                ID4 += 1
            elif Class_ID == 5:
                ID5 += 1
            elif Class_ID == 6:
                ID6 += 1
                print(labels)
            else:
                empty += 1


if __name__ == '__main__':
    labels = get_file_path('C:/Users/user/Desktop/archive/day/train/labels')
    for i in range(len(labels)):
        copy_file(labels[i])

    # labels = GetFilePath('C:/Users/user/Desktop/archive/day/val/labels')
    # for i in range(len(labels)):
    #     Copyfile(labels[i])

    print(
        f'go: {ID0} stop:{ID1} warning:{ID2} stopLeft:{ID3} goLeft:{ID4} warningLeft:{ID5} goForward:{ID6} empty:{empty}')
