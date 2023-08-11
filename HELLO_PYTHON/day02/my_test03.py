# 출력할 단수를 입력하시오. 4
# 4*1 = 4
# 4*2 = 8 
#   :
# 4*9 = 36

a = int(input("출력할 단수를 입력하시오."))
arr = list(range(1, 9+1))

for i in arr:
    print(str(a) + "*" + str(i) + "=" + str(a*i));