class Animal:
    def __init__(self): # 생성자
        self.age = 1
    
    
    def birthHappy(self):
        self.age += 1 # ++, --, !, &&, || 는 사용불가
        


# 이렇게 실행하면 다른 곳에서 호출해도 출력되지 않음(메인 선언)
if __name__ == '__main__' :
    ani = Animal()
    print("11", ani.age)
    ani.birthHappy()
    print("11", ani.age)
         

