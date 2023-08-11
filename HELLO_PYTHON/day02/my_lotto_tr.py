# 1~45까지의 숫자 중에서 6개의 숫자를 중복없이 뽑기
from random import random

arr =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
      11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
      21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
      31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
      41, 42, 43, 44, 45]


for i in range(100):
    rnd = int(random()*45)
    a = arr[rnd]
    b = arr[0]
    arr[0] = a
    arr[rnd] = b
    
print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])
print(arr[0:6]) #배열을 잘라주는 역할