class DbClient:
    def __init__(self, filename):
        try:
            f = open(filename, "r")
            self.login = f.read(10)
            self.pwd = f.read(20)
        except Exception as exc:
            print(f"Error {exc}")
	finally: # продолжить что-то в любом случае
    	    f.close()

bd = DbClient("txt.txt")



try:
    pass
finally: # продолжить что-то в любом случае
    pass
    #do something 