# Классовый метод

class Employee:
    count = 0

    def __new__(cls):
        cls.count+=1
        return super().__new__(cls)

    @classmethod # метод класса работает только с атрибутами
    def get_count(self):
        return self.count

    @staticmethod # ничего не принимает, не работает с атрибутами, но связан с классом
    def say():
        print("hello")



p1 = Employee()
print(p1.get_count())