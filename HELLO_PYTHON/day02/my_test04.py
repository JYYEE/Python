# 1~9사이의 숫자 중 중복없이 3개의 숫자를 선택하세요.
from random import random

arr =[1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 3+1) : 
    rnd = random()
    idx = int(rnd *10)
    a = arr[idx]
    print(a)
    arr.remove(a)
    