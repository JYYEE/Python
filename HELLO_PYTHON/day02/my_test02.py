# 첫수를 입력하시오. 5
# 끝수를 입력하시오. 7
# 5에서 7까지 합은 18입니다.

start = int(input("첫 수를 입력하시오."))
end = int(input("끝 수를 입력하시오."))

arr = list(range(start, end+1))
print(arr)
sum = 0
for i in arr :
    sum +=i 

print("sum : ",sum)
print("sum : " + str(sum))