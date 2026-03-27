import os
import sys

name = sys.argv[1]

path = os.path.expanduser("~") + "/" + name

if os.path.exists(path):
    if os.path.isdir(path):
        files = os.listdir(path)
        if len(files) == 0:
            os.rmdir(path)
            print("Удалил папку")
        else:
            print("Папка не пустая")
    else:
        print("Это не папка")
else:
    print("Папка не найдена")