from day03.my_oop01 import Animal
class Human(Animal) : # Human이 Animal을 상속
    # self넣는 것은 기본 문법이라 생략 불가
    def __init__(self):
        super().__init__() # 부모의 생성자를 불러옴
        self.tools = []
        self.tools.append("ring")
        
    def farming(self, tool):
        self.tools.append(tool)
        
    def __str__(self):
        ret=str(self.tools)
        return ret
    
    
hum = Human()
print(hum.age)
print(hum)
hum.birthHappy()
hum.farming("ax")
print(hum.age)
print(hum)
