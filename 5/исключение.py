class DbClient:
    def __init__(self, filename):
        try:
            f = open(filename, "r")
            self.login = f.read(10)
            self.pwd = f.read(20)
        except Exception as exc:
            print(f"Error {exc}")
	finally: # ���������� ���-�� � ����� ������
    	    f.close()

bd = DbClient("txt.txt")



try:
    pass
finally: # ���������� ���-�� � ����� ������
    pass
    #do something 