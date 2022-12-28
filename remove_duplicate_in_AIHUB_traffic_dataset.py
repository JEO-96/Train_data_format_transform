"""
AIHUB 교통신호/표지판 데이터셋에서 중복되는 레이블 제거
"""
import json
import os


def remove_duplicate(path):
    file_list = os.listdir(path)
    file_list_json = [file for file in file_list if file.endswith('.json')]

    for f_json in file_list_json:
        json_file_name = path + '/' + f_json

        with open(json_file_name, "r") as st_json:
            st_python = json.load(st_json)
            # 생성할 파일 이름
            with open(json_file_name, 'w') as make_file:
                new_list = []
                for v in st_python['annotation']:
                    if v not in new_list:
                        new_list.append(v)
                st_python['annotation'] = new_list
                json.dump(st_python, make_file)
            print(json_file_name)


if __name__ == '__main__':
    remove_duplicate(r'G:\py_json\train\jsons')
    remove_duplicate(r'G:\py_json\val\jsons')
