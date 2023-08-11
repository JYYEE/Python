# 가위/바위/보를 선택하세요 
# 나 : 가위
# 컴 : 바위
# 결과 : 패배
from random import random

rnd = random()

myres = input("가위/바위/보를 선택하세요.")
comres = ""
result = ""

if rnd<0.33 : 
    comres = "가위"
elif rnd>=0.66 :
    comres = "보"
else : 
    comres = "바위"

if myres == comres :
    result ="비겼다."
elif (myres == "가위" and comres == "보" )or (myres == "보" and comres == "바위" ) or (myres == "바위" and comres == "가위" ) :
    result ="이겼다."
else :
    result ="졌다."
    
print("나 : ", myres)
print("컴 : ", comres)
print("결과 : ", result)
    