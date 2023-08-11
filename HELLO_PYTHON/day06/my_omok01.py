# ui파일을 파이썬에 연결시키기
# 단, UI 파일은 python코드 파일과 같은 디렉토리에 위치
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap, QIcon, QPushButton, QSize

form_class = uic.loadUiType("my_omok01.ui")[0] # ui 파일명

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) : #QMainWindow, form_class 상속. 
    #초기화 메서드
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.flag_dol= True
        for i in range(10):
            for j in range(10):
                temp = QPushButton('',self)
                temp.setIcon(QIcon("0.png"))
                temp.setIconSize(QSize(40,40))
                temp.setGeometry(i*40,j*40,40,40)
                temp.clicked.connect(self.myclick)
        
        
        
    def myclick(self):
        if self.flag_dol:
            self.sender().setIcon(QIcon("1.png"))
        else :
            self.sender().setIcon(QIcon("2.png"))
        
        self.flag_dol = not self.flag_dol
        
        # pixmap = QPixmap("1.png")
        # icon = QIcon()
        # icon.addPixmap(pixmap)
        # self.pb.setIcon(icon)
    
         
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv) #QApplication : 프로그램을 실행시켜주는 클래스. window실행시키는 
    myWindow = WindowClass() # WindowClass의 인스턴스 생성
    myWindow.show() # 프로그램 화면을 보여주는 코드
    app.exec_() # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드