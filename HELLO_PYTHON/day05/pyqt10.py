# ui파일을 파이썬에 연결시키기
# 단, UI 파일은 python코드 파일과 같은 디렉토리에 위치
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt10.ui")[0] # ui 파일명

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) : #QMainWindow, form_class 상속. 
    #초기화 메서드
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # 버튼에 기능을 연결(self.버튼이름.clicked.connect(self.버튼클릭메소드명))
        self.pb.clicked.connect(self.myclick)
        
    def getStar(self, cnt):
        ret =""
        for i in range(cnt):
            ret += "*"
        
        ret +="\n"
        return ret


    # pb가 눌리면 작동할 함수 
    def myclick(self):
        a = self.le_first.text()
        b = self.le_last.text()
        
        ia = int(a)
        ib = int(b)
        
        res = ""
        
        for i in range(ia, ib+1):
            res += self.getStar(i) #매개변수 넘기는 방법
        
        # 이중for문 가독성 떨어짐 => 함수로 만들기
        # for i in range(ia, ib+1):
        #     for j in range(i):
        #         res +="*"
        #
        #     res +="\n"
        #
        
        self.te.setText(res)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) #QApplication : 프로그램을 실행시켜주는 클래스. window실행시키는 
    myWindow = WindowClass() # WindowClass의 인스턴스 생성
    myWindow.show() # 프로그램 화면을 보여주는 코드
    app.exec_() # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    
    