# Property

class Singleton:
    obj = None

    def __new__(cls):
        if cls.obj == None:
            cls.obj = super().__init__(cls)
	    cls.obj.db = sqlite = connect()
        return cls.obj

s1 = Singleton()
s2 = Singleton()
s1.db #что-то будет открыто из двух
s2.db
assert(id(s1) == id(s2)) #true