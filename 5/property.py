#Property

class Person:
    def __init__(self, salary):
        self.__salary = salary #����������� ��������� ��� ����������

    @property #getter
    def salary(self):
        return self.__salary

    @salary.setter #setter
    def salary(self, salary):
        if isinstance(salary, int):
            self.__salary += salary
        else:
            print("Error")

p = Person(100)
p.salary = 100
print(p.salary)
