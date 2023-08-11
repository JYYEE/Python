# 홀/짝 프로그램
# 홀/짝을 입력하시오. - 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 승리
from random import random

myres = input("홀/짝을 입력하시오.")
print("나 : " + myres)

rnd = random()
if rnd >= 0.5 :
    comres = "홀"
else :
    comres = "짝"
print("컴 : " + comres)

if myres == comres : 
    result = "승리"
else :
    result = "패배" 
print("결과 : " + result)