#Пузырьковая сортировка
arr = [1,5,3,6,8,7,2]
for i in range(len(arr) - 1, 0 , -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j],arr[i] = arr[i], arr[j]
print(arr)