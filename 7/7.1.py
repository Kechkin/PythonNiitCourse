import datetime

def count_date(y,m,d, y2,m2,d2):
	first = datetime.date(y,m,d)
	last = datetime.date(y2,m2,d2)
	return last - first

print(count_date(2021, 1, 27, 2021, 1, 30))

