# 자바와 다른 점
# 소멸자 존재
# 생성자를 메모리에서 지워주는 역할
# 자바에서는 가비지 콜렉터가 존재해서 소멸할 필요 없지만 다른 언어들은 지워줘서 메모리 비워줘야함.
class Biden:
    def __init__(self):
        print("생성자")
        
    def ira(self):
        print("ira")
        
    def __del__(self):
        print("소멸자")
        

b=Biden()
b.ira()
# 메소드 실행된 이후에 바로 소멸됨.