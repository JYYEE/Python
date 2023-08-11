# 구구단 출력하는 함수 만들기
def showDan(dan):
    print(str(dan) + "단")
    for i in range(1,10) : 
        #print(str(dan) + "*" +str(i) + " = " + str(i*dan))
        # format이용
         print("{}*{}={}".format(dan, i, dan*i)) 
        
showDan(6)