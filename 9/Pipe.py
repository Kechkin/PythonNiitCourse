from multiprocessing import Process, Pipe

def f(conn):
	conn.send(['hello', 11, "from"]) #можно переслать только сереализуемые данные Pickle
	print(f"Client receives:{conn.recv()}")

if __name__=='__main__':
	parent_conn, child_conn = Pipe() # возвращ. кортеж(parent_conn ( передавать),  child_conn(получать))
	p = Process(target=f, args=(child_conn,)) #f будет принимать знач(child_conn)
	p.start()


	print(f"From Server{parent_conn.recv()}") #получить .revc - блокирующий, ждет ответа от f
	parent_conn.send(['py', 3])
	p.join()