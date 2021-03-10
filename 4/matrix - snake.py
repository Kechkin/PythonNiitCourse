#заполнение змейкой

row = 5
colomn = 6

tab = [[0] * colomn for _ in range(row)]
index = 0

for i in range(row):
    if i % 2 == 0:
        for x in range(0, colomn):
            index+=1
            tab[i][x] = index
    else:
        for x in range(colomn -1, -1, -1):
            index+=1
            tab[i][x] = index
        
for i in tab:
    print(*i)
