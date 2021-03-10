# ��������� �����

class Employee:
    count = 0

    def __new__(cls):
        cls.count+=1
        return super().__new__(cls)

    @classmethod # ����� ������ �������� ������ � ����������
    def get_count(self):
        return self.count

    @staticmethod # ������ �� ���������, �� �������� � ����������, �� ������ � �������
    def say():
        print("hello")



p1 = Employee()
print(p1.get_count())