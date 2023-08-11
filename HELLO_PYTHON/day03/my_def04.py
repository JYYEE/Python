# 멀티리턴
def add_min_mul_div_nam(a, b):
    return a+b, a-b, a*b, a/b, a%b

a,b,c,d,e = add_min_mul_div_nam(4, 3)
f =add_min_mul_div_nam(4, 3)
print(a,b,c,d,e)
print(f) # 튜플 - ()안에 결과값 닮김. 배열과 비슷함.