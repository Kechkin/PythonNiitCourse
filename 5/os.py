import os

file = os.path.join('tmp', 'file.txt') #для поиска файла автоматически
if os.path.exists(file):
    with open("tmp/file.txt") as f:
        print(f.read())



import os
import shutil

for i in os.listdir('.'): # просмотр всего каталога
    if os.path.isfile(i):  # проверка на папку
        print(f"{i} - file")
    else:
        print(f"{i} - dir")
