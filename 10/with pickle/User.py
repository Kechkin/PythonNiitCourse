class User:
    def __init__(self):
        self.name = "default"
        self.age= 111001
        self.place = "LAX"

    def __repr__(self):
        return f"User : {self.name}, { self.age} {self.place}"