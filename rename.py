import os


def rollback_word(path):
    files = os.listdir(path)
    for i in files:
        file_old_name = os.path.join(path, i)
        file_new_name = os.path.join(path, i[1:])
        os.rename(file_old_name, file_new_name)


def add_word(path, s):
    files = os.listdir(path)
    for i in files:
        file_old_name = os.path.join(path, i)
        file_new_name = os.path.join(path, s + i)
        os.rename(file_old_name, file_new_name)


if __name__ == '__main__':
    add_word(r'\\DESKTOP-D8HC3HJ\Server\Virtual_Data\CARLA_ClearNoon_2\ClearNoonTown10\images', "10")
    add_word(r'\\DESKTOP-D8HC3HJ\Server\Virtual_Data\CARLA_ClearNoon_2\ClearNoonTown10\labels', "10")
    # rollback_word(r'\\DESKTOP-D8HC3HJ\Server\Virtual_Data\CARLA_ClearNoon_2\ClearNoonTown01\images')