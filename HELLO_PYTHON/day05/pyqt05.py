# ui파일을 파이썬에 연결시키기
# 단, UI 파일은 python코드 파일과 같은 디렉토리에 위치
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0] # ui 파일명

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) : #QMainWindow, form_class 상속. 
    #초기화 메서드
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # 버튼에 기능을 연결(self.버튼이름.clicked.connect(self.버튼클릭메소드명))
        self.pb.clicked.connect(self.myclick)
    
    # pb가 눌리면 작동할 함수 
    def myclick(self):
        arr=[1,2,3,4,5,6,7,8,9,10,
             11,12,13,14,15,16,17,18,19,20,
             21,22,23,24,25,26,27,28,29,30,
             31,32,33,34,35,36,37,38,39,40,
             41,42,43,44,45]
        for i in range(45):
            rnd = int(random()*45)
            a= arr[i]
            b= arr[rnd]
            arr[i]=b 
            arr[rnd]=a
            
        self.te1.setText(str(arr[0]))
        self.te2.setText(str(arr[1]))
        self.te3.setText(str(arr[2]))
        self.te4.setText(str(arr[3]))
        self.te5.setText(str(arr[4]))
        self.te6.setText(str(arr[5]))
        
if __name__ == "__main__":
    app = QApplication(sys.argv) #QApplication : 프로그램을 실행시켜주는 클래스. window실행시키는 
    myWindow = WindowClass() # WindowClass의 인스턴스 생성
    myWindow.show() # 프로그램 화면을 보여주는 코드
    app.exec_() # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    
    