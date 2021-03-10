import threading


class MyThread(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.__data = data

    def run(self):
        print(f"Thread's name: {threading.current_thread().name}, data: {self.__data}")


thr_arr = [MyThread("text"), MyThread(521), MyThread([1,2,3,4]), MyThread("string")]

for i in thr_arr:
    i.start()

for i in thr_arr:
    i.join()

