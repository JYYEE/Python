# ui파일을 파이썬에 연결시키기
# 단, UI 파일은 python코드 파일과 같은 디렉토리에 위치
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap, QIcon, QPushButton, QSize
from _ast import If

form_class = uic.loadUiType("my_omok02.ui")[0] # ui 파일명

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) : #QMainWindow, form_class 상속. 
    #초기화 메서드
    def __init__(self) :
        super().__init__()
        self.flag_dol= True
        self.flag_over = False
        # 바둑판 역할
        self.arr2D =[ 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.pbs=[]
        
        self.setupUi(self)
        self.pb.clicked.connect(self.myreset)
        
        for i in range(10):
            for j in range(10):
                temp = QPushButton('',self)
                temp.setToolTip("{},{}".format(i, j))
                temp.setIcon(QIcon("0.png"))
                temp.setIconSize(QSize(40,40))
                temp.setGeometry(j*40,i*40,40,40)
                temp.clicked.connect(self.myclick)
                self.pbs.append(temp)
                
        self.myrender()
        
    def myreset(self):
        for i in range(10):
            for j in range(10):
                self.arr2D[i][j] = 0
       
        self.myrender();
        self.flag_over = False
        self.flag_dol = True
        
    def myrender(self):
        for i in range(10): 
            for j in range(10):
                if self.arr2D[i][j] ==0 :
                    self.pbs[10*i+j].setIcon(QIcon("0.png"))
                if self.arr2D[i][j] ==1 :
                    self.pbs[10*i+j].setIcon(QIcon("1.png"))
                if self.arr2D[i][j] ==2 :
                    self.pbs[10*i+j].setIcon(QIcon("2.png"))
    
    
    def myclick(self):
        if self.flag_over:
            return 
        # sender() 이용
        #i, j 구하기
        i = self.sender().toolTip().split(',')[0]
        j = self.sender().toolTip().split(',')[1]
        ii = int(i)
        jj = int(j)
        
        if self.arr2D[ii][jj] > 0:
            return
        
        stone = -1
        if self.flag_dol:
            self.arr2D[ii][jj] =1
            stone = 1
        else :
            self.arr2D[ii][jj] =2
            stone = 2
            
        up = self.checkUP(ii,jj, stone)
        dw = self.checkDW(ii,jj, stone)
        le = self.checkLE(ii,jj, stone)
        ri = self.checkRI(ii,jj, stone)
        ur = self.checkUR(ii,jj, stone)
        dr = self.checkDR(ii,jj, stone)
        ul = self.checkUL(ii,jj, stone)
        dl = self.checkDL(ii,jj, stone)

        self.myrender()
        
        d1 = up + dw + 1
        d2 = le + ri + 1
        d3 = ur + dl + 1
        d4 = dr + ul + 1
        
        if (d1 == 5) or (d2 == 5) or (d3 == 5) or (d4 == 5) :
            self.flag_over = True
            if self.flag_dol : # stone, self.flag_dol 다 가능하지만 전역변수를 사용
                res ="흑"
            else:
                res ="백"
            QMessageBox.about(self, '오목 완성' , res+'돌 승리!!!') 

        self.flag_dol = not self.flag_dol
        
        
    # 위
    def checkUP(self, ii, jj, stone):
        cnt =0
        try:
            while True:
                ii -=1
                if ii<0 or jj<0:
                    return cnt
                if self.arr2D[ii][jj] == stone:
                    cnt +=1
                else : 
                    return cnt 
        except:
            return cnt
            
    # 아래    
    def checkDW(self, ii, jj, stone):
        cnt =0
        try:
            while True:
                ii +=1
                if ii<0 or jj<0:
                    return cnt
                if self.arr2D[ii][jj] == stone:
                    cnt +=1
                else : 
                    return cnt 
        except:
            return cnt
    
    # 왼쪽
    def checkLE(self, ii, jj, stone):
        cnt =0
        try:
            while True:
                jj -=1
                if ii<0 or jj<0:
                    return cnt
                if self.arr2D[ii][jj] == stone:
                    cnt +=1
                else : 
                    return cnt 
        except:
            return cnt
    
    # 오른쪽
    def checkRI(self, ii, jj, stone):
        cnt =0
        try:
            while True:
                jj +=1
                if ii<0 or jj<0:
                    return cnt
                if self.arr2D[ii][jj] == stone:
                    cnt +=1
                else : 
                    return cnt 
        except:
            return cnt
            
    # 우상        
    def checkUR(self, ii, jj, stone):
        cnt =0
        try:
            while True:
                ii -=1
                jj +=1
                if ii<0 or jj<0:
                    return cnt
                if self.arr2D[ii][jj] == stone:
                    cnt +=1
                else : 
                    return cnt 
        except:
            return cnt
    
    # 우하        
    def checkDR(self, ii, jj, stone):
        cnt =0
        try:
            while True:
                ii +=1
                jj +=1
                if ii<0 or jj<0:
                    return cnt
                if self.arr2D[ii][jj] == stone:
                    cnt +=1
                else : 
                    return cnt 
        except:
            return cnt
    
    # 좌상        
    def checkUL(self, ii, jj, stone):
        cnt =0
        try:
            while True:
                ii -=1
                jj -=1
                if ii<0 or jj<0:
                    return cnt
                if self.arr2D[ii][jj] == stone:
                    cnt +=1
                else : 
                    return cnt 
        except:
            return cnt
    
    # 좌하        
    def checkDL(self, ii, jj, stone):
        cnt =0
        try:
            while True:
                ii +=1
                jj -=1
                if ii<0 or jj<0:
                    return cnt
                if self.arr2D[ii][jj] == stone:
                    cnt +=1
                else : 
                    return cnt 
        except:
            return cnt
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv) #QApplication : 프로그램을 실행시켜주는 클래스. window실행시키는 
    myWindow = WindowClass() # WindowClass의 인스턴스 생성
    myWindow.show() # 프로그램 화면을 보여주는 코드
    app.exec_() # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드