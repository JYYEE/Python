# for i in range(2,10):
#     for j in range(1,10):
#         print("{}*{}={}".format(i, j, i*j))
#


def dan(num):
    res = ""
    for i in range(1,10):
        res = "{}*{}={}".format(num,i,num*i)
        print(res)
    return res
    
    
    
def gugudan():
    res2 = ""
    # for j in range(9, 1, -1):
    #     if(not(j % 3 == 0 or j % 5 ==0)):
    #         res2 += dan(j)
    res2 += dan(9)
    res2 += dan(7)
    res2 += dan(3)
    res2 += dan(2)
    return res2

if __name__ == "__main__":
    gugudan()
    
## 이중for문은 필요할 때만 쓰고 최대한 쓰지 말기 -> 최대한 메소드로 유도  
    
    
    
def showdan(dan):
    print("{}*{}={}".format(dan, 1, dan*1))    
    print("{}*{}={}".format(dan, 2, dan*2))    
    print("{}*{}={}".format(dan, 3, dan*3))    
    print("{}*{}={}".format(dan, 4, dan*4))    
    #print("{}*{}={}".format(dan, 5, dan*5))    
    print("{}*{}={}".format(dan, 6, dan*6))    
    print("{}*{}={}".format(dan, 7, dan*7))    
    print("{}*{}={}".format(dan, 8, dan*8))    
    print("{}*{}={}".format(dan, 9, dan*9)) 
    
showdan(9)
showdan(7)
showdan(3)
showdan(2)   