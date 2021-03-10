from threading import Thread


def mysum(*args):

    lst = []
    for i in args:
        if isinstance(i, int):
            print(sum(args))
            return sum(args)
        elif isinstance(i, str):
            print("".join(list(args)))
            return "".join(list(args))
        elif isinstance(i, list):
            for x in i:
                lst.append(x)
    print(lst)
    return lst


thr_arr = [Thread(target=mysum, args=(2, 4, 3, 2, 4, 9, 6)),
           Thread(target=mysum, args=("one", "two", "three")),
           Thread(target=mysum, args=([1, 3, 4], [5, 6, 7], [8, 9, 0]))]

for i in thr_arr:
    i.start()

for i in thr_arr:
    i.join()

