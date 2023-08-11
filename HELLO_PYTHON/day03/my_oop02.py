from day03.my_oop01 import Animal
# import 되면서 my_oop01파일 실행됨 -> 연습삼아 출력했던것들 다 출력됨
# 이를 방지하고자 my_oop01파일에서 메인 작성
ani = Animal()

print(ani.age)
ani.birthHappy()
print(ani.age)

