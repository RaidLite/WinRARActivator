import os
import shutil

def activate(d):
    path = os.path.join(d, 'rarreg.key')
    if os.path.isfile(path):
        v = input('Файл существует. Перезаписать? [y/n] >>> ').lower()
        if v != 'y': return print('Отказ от записи')
        try: os.remove(path)
        except: return print('Нужны права админа')

    try:
        shutil.move('rarreg.key', d)
        print('WinRAR успешно активирован')
    except: print('Ошибка активации (права админа или файл не найден)')

def main():
    while True:
        print("1. Activate WinRAR")
        print(" ")
        match input('>>> '):
            case 1: activate('C:\Program Files\WinRAR')

if __name__ == '__main__':
    main()