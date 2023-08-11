# 홀/짝 프로그램
# 홀/짝을 입력하시오. - 홀
# 나 : 홀
# 컴 : 홀
# 결과 : 승리
from random import random

mine = ""
com = ""
result = ""

mine = input("홀/짝을 입력하시오.")
rnd = random()

if rnd > 0.5 :
    com = "홀"
else : 
    com = "짝"
    
if mine == com:
    result = "승리"
else : 
    result = "패배"

#print("나 : " + mine) # 자바 스크립트에서 console.log(a, b, c)로 하는 것과 같이 할 수 있음.
#print()는 기본 개행. 개행하지 않으려면 print("나", end="") 
#end="" ""사이에 뭔가 넣어주면 그걸 맨 마지막에 출력해준다. ex) end="\t" 뒤에 탭을 넣어줌.
print("나 : ", mine) 
print("컴 : ", com)
print("결과 : " , result)