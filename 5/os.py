import os

file = os.path.join('tmp', 'file.txt') #��� ������ ����� �������������
if os.path.exists(file):
    with open("tmp/file.txt") as f:
        print(f.read())



import os
import shutil

for i in os.listdir('.'): # �������� ����� ��������
    if os.path.isfile(i):  # �������� �� �����
        print(f"{i} - file")
    else:
        print(f"{i} - dir")
