# 함수 (메소드 역할)
# 자바 스크립트에서 function 대신에 def쓰는 것.
# add(4,3)보다 함수의 정의가 더 아래쪽에 있으면 오류.
# 자바는 컴파일 언어라 미리 메소드를 만들어 두고 사용하므로 메소드가 아래에 있어도 실행되지만
# 파이썬은 인터프리터 언어(ex. 자바 스크립트)라 위에서부터 읽어들어오는 구조라 위에서 정의하고 아래에서 사용해야지 실행가능.

def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def namuji(a, b):
    return a%b

sum = add(4, 3)
min = minus(4, 3)
mul = multiply(4, 3)
div = divide(4, 3)
nam = namuji(4,3)

print("sum : ", sum)
print("min : ", min)
print("mul : ", mul)
print("div : ", div)
print("nam : ", nam)