import pickle


class Man:
    
   name = "ivan"
    
   salary = 2000
    


m = Man()
with open("file.txt", "wb") as f:
     #wb - �������� �����
   pickle.dump(m, f) #f - file
 #��������� ������