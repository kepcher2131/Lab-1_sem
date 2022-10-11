# Задан массив целых чисел А(20). Все элементы, кратные числу К, заменить на нуль.
from random import randint
arr = []
k = int(input())
for i in range(20):
    arr.append(randint(-100,100))
print(arr)

for i in range(20):
    if arr[i]%k==0:
        arr[i] = 0
print(arr)
