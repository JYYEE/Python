# 첫 수를 입력하시오. 1
# 끝 수를 입력하시오. 10
# 배수를 입력하시오. 5
# 1에서 10까지의 5의 배수의 합은 15입니다.

a = input("첫수를 입력하시오.")
b = input("끝수를 입력하시오.")
c = input("배수를 입력하시오.")

ia = int(a)
ib = int(b)
ic = int(c)
sum = 0;

for i in range(ia,ib+1):
    if(i%ic == 0):
        sum += i
        print(i)
    

print("{}에서 {}까지의 {}의 배수의 합은 {}입니다.".format(a, b, c, sum))