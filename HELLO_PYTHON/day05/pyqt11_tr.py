# ui파일을 파이썬에 연결시키기
# 단, UI 파일은 python코드 파일과 같은 디렉토리에 위치
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt11.ui")[0] # ui 파일명

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) : #QMainWindow, form_class 상속. 
    #초기화 메서드
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.com = "" # 멤버변수로 생각.(전역변수)
        self.setRandomCom()
        # 버튼에 기능을 연결(self.버튼이름.clicked.connect(self.버튼클릭메소드명))
        self.pb.clicked.connect(self.myclick)
    
    def setRandomCom(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(100):
            rnd = int(random()*9)
            m = arr[0]
            n = arr[rnd]
            arr[0] = n
            arr[rnd] = m
        self.com = str(arr[0])+str(arr[1])+str(arr[2])
    
    # pb가 눌리면 작동할 함수 
    def myclick(self):
        c1 = self.com[0:1]
        c2 = self.com[1:2]
        c3 = self.com[2:3]
        
        a = self.le.text()
        a1 = a[0:1]
        a2 = a[1:2]
        a3 = a[2:3]
        
        scnt = 0
        bcnt = 0
        if c1 == a1 :
            scnt += 1
        if c2 == a2 :
            scnt += 1
        if c3 == a3 :
            scnt += 1

        if c1 == a2 or c1 == a3 :
            bcnt += 1
        if c2 == a1 or c2 == a3 :
            bcnt += 1
        if c3 == a1 or c3 == a2 :
            bcnt += 1
        
        res =self.pte.toPlainText()
        res += a + "\t"+str(scnt)+"S"+str(bcnt)+"B\n"
        self.le.setText("")
        self.pte.setPlainText(res)
        
        if scnt == 3 :
            QMessageBox.about(self,'성공' , a+ ' 맞췄습니다') 
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) #QApplication : 프로그램을 실행시켜주는 클래스. window실행시키는 
    myWindow = WindowClass() # WindowClass의 인스턴스 생성
    myWindow.show() # 프로그램 화면을 보여주는 코드
    app.exec_() # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    
    