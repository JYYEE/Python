# ui파일을 파이썬에 연결시키기
# 단, UI 파일은 python코드 파일과 같은 디렉토리에 위치
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt08.ui")[0] # ui 파일명

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
        a = self.le.text()
        ia = int(a)
        res = ""
        for i in range(1,9+1):
            mul = ia*i
            res += a+"*" +str(i) +"=" + str(mul) +"\n"
            #res += "{}*{}={}\n".format(ia, i, ia*i)
        
        print(res)
        # pte로 받아서 정의하면 .으로 메소드 호출 가능
        #pte = QPlainTextEdit()
        #pte.setPlainText()
        self.pte.setPlainText(res)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) #QApplication : 프로그램을 실행시켜주는 클래스. window실행시키는 
    myWindow = WindowClass() # WindowClass의 인스턴스 생성
    myWindow.show() # 프로그램 화면을 보여주는 코드
    app.exec_() # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    
    