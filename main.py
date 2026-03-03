import os
import shutil
import sys

PATH_WinRAR = r'C:\Program Files\WinRAR'
KEY_FILE = 'rarreg.key'

def activate(dir):
    path = os.path.join(dir, KEY_FILE)
    if os.path.isfile(path):
        if input('Файл существует. Перезаписать? [y/n] >>> ').lower() != 'y':
            return print('Отказ от записи')
        try:
            os.remove(path)
        except:
            return print('Нужны права админа')

    try:
        shutil.copy(KEY_FILE, dir)
        print('WinRAR успешно активирован')
    except:
        print('Ошибка активации (права админа или файл не найден)')

def main():
    while True:
        print(" ")
        print("1. Activate WinRAR")
        print("0. Exit")
        print(" ")
        match int(input('>>> ')):
            case 1: activate(PATH_WinRAR)
            case 0: sys.exit(0)

if __name__ == '__main__':
    main()