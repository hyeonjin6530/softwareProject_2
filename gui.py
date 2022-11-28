from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLineEdit,QLabel,QGridLayout
from PyQt5.QtWidgets import QTextEdit,QHBoxLayout,QVBoxLayout


class ethnicOfHaksik(QWidget):
    
    def __init__(self,parent = None):
        super().__init__(parent)
    
        tableLayout = QGridLayout()

        days = ["   ","Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

        for i in range(len(days)):
            box = QLineEdit()
            box.setReadOnly(True)
            box.setAlignment(Qt.AlignCenter)
            box.setText(days[i])
            box.setFixedWidth(50)
            tableLayout.addWidget(box,0, i)
        
        for i in range(9,20):
            box = QLineEdit()
            box.setReadOnly(True)
            box.setAlignment(Qt.AlignRight)
            box.setText(str(i%12))
            box.setFixedWidth(50)
            tableLayout.addWidget(box,i-8,0)
            for j in range(7):
                button = QPushButton()
                button.setFixedWidth(50)
                button.setCheckable(True)
                button.toggled.connect(self.slot_toggle)
                button.toggle()
                tableLayout.addWidget(button,i-8,j+1)

# 여기까지 시간표 ******************************************
        timetableLable = QLabel('시간표를 입력해주세요!', self) 
        foodLable = QLabel('지금 먹을 수 있는 학식은..', self)

        showButton = QPushButton("Show", self)

        self.resultBox = QTextEdit(self)

        showButton.clicked.connect(self.showClicked)


        hbox1 = QHBoxLayout()
        hbox1.addWidget(foodLable)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(timetableLable)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(showButton)

        vbox = QVBoxLayout()
        vbox.addWidget(self.resultBox)
        vbox.addLayout(hbox3)

        #self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('학식의 민족')   
        mainLayout = QGridLayout()
        mainLayout.addLayout(hbox2, 0, 0)
        mainLayout.addLayout(tableLayout, 1, 0)
        mainLayout.addLayout(hbox1, 0, 1)
        mainLayout.addLayout(vbox, 1, 1)
        self.setLayout(mainLayout)
         
    def slot_toggle(self,state):

        button = self.sender()
        button.setStyleSheet("background-color: %s" % ({True: "green", False: "red"}[state]))
        
    def showClicked(self):
        pass  # 나중에 여기서 웹크롤링한 결과를 출력
if __name__ == '__main__':
    
    import sys
    app = QApplication(sys.argv)
    application = ethnicOfHaksik()
    application.show()
    sys.exit(app.exec_())