'''Asyncio для работы с асинхрон. операциями'''
#один поток
import asyncio

res = 0


async def calc(num): #
	global res
	while num > 0:
		print(num)
		if num % 10 == 0:
			res = num
		num-=1
		await asyncio.sleep(0.1)

async def status():
	global res
	prev_rs = 0
	while res > 0:
		if res != prev_rs:
			print(f"{res} number remain")
			prev_rs = res
		await asyncio.sleep(0.1)

if __name__ == '__main__':

	ev_loop = asyncio.get_event_loop()
	tasks = [ev_loop.create_task(calc(1000)), 
				ev_loop.create_task(status())]
	futures = asyncio.wait(tasks)
	ev_loop.run_until_complete(futures)
	ev_loop.close()
