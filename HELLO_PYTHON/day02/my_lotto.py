# 1~45까지의 숫자 중에서 6개의 숫자를 중복없이 뽑기
from random import random


arr=[];
for i in range(1, 45+1):
    arr.append(i)

for i in range(100):
    rnd = int(random()*45)
    a = arr[rnd]
    b = arr[0]
    arr[0] = a
    arr[rnd] = b

for i in range(6): 
    print(arr[i])