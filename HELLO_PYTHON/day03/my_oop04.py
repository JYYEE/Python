# 다중 상속
# 
from day03.my_oop03 import Human
class LeeJY:
    def __init__(self):
        self.cnt_company = 20
        
    def seat(self):
        self.cnt_company +=1
        
class Bin:
    def __init__(self):
        self.amount_oil = 10000
        
    def dig(self):
        self.amount_oil *= 2
        
class KimJE:
    def __init__(self):
        self.cnt_nuclear = 30
        
    def aoji(self):
        self.cnt_nuclear += 2
        
class KimJW(LeeJY, Bin, KimJE):
    def __init__(self):
        # 다중상속에서는 super().__init__()을 쓰면 맨 처음것만 상속받음.
        # 다중상속에서는 클래스.__init__(self) 로 작성.
        KimJE.__init__(self) 
        Bin.__init__(self)
        LeeJY.__init__(self)

a = KimJW()
print(a.cnt_company)
a.seat()
print(a.cnt_company)

print(a.amount_oil)
a.dig()
print(a.amount_oil)

print(a.cnt_nuclear)
a.aoji()
print(a.cnt_nuclear)
    