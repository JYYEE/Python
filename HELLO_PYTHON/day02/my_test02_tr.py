# 첫수를 입력하시오. 5
# 끝수를 입력하시오. 7
# 5에서 7까지 합은 18입니다.

a = input("첫 수를 입력하시오.")
b = input("끝 수를 입력하시오.")
aa = int(a)
bb = int(b)
mylist = list(range(aa, bb+1))

sum = 0
for i in mylist :
    sum +=i 

print(a+"에서 " + b+"까지 합은 " + str(sum)+"입니다.")
print("{}에서 {}까지 합은 {}입니다.".format(a, b, sum))