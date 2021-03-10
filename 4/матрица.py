#удалить из столбец из списка где присутствует число

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9,]
        ]
def delColomn(matrix):
    n = 1
    pos = 0
    
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if n == matrix[i][j]:
                pos = j
                
    for i in matrix:
        i.pop(pos)
        
    for i in matrix:
        print(i)
print(delColomn(matrix))