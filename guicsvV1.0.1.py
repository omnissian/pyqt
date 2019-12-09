from tkinter import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import os
import codecs

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title="BridgesCSVv1"
        self.left=400
        self.top=300
        self.width=768
        self.height=200
        self.initUI()
    def initUI(self):
        # self.filter="*.csv"
        self.fchosen=False
        self.header=False
        self.filter="*.*"
        self.file_name="Choose *.CSV file"
        self.qlfname=QLabel(self.file_name)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height) #left right bottom top
        grid=QGridLayout()
        button_1=QPushButton("Open file",self)
        button_1.setToolTip("Are you sure about that")
        button_1.move(0,0)
        button_1.clicked.connect(self.button_1_clicked)
        button_saver=QPushButton("Add",self)
        button_saver.clicked.connect(self.button_saver_clicked)
        bridgenamelabel=QLabel("Bridge Name")
        leftLabel=QLabel("Left Coordinates")
        rightLabel=QLabel("Right Coordinates")
        bottomLabel=QLabel("Bottom Coordinates")
        topLabel=QLabel("Top Coordinates")
        self.bridgename=QLineEdit("Bridge Name")
        self.left=QLineEdit("Left Coordinates")
        self.left.setValidator(QDoubleValidator())
        self.right=QLineEdit("Right Coordinates")
        self.right.setValidator(QDoubleValidator())
        self.bottom=QLineEdit("Bottom Coordinates")
        self.bottom.setValidator(QDoubleValidator())
        self.top=QLineEdit("Top Coordinates")
        self.top.setValidator(QDoubleValidator())
        #---------grid-----------
        box_all=QVBoxLayout()
        box_all.addWidget(button_1,Qt.AlignTop | Qt.AlignLeft)
        box_all.addWidget(self.qlfname, Qt.AlignTop | Qt.AlignLeft)
        grid.addWidget(bridgenamelabel,3,1,Qt.AlignCenter)
        grid.addWidget(leftLabel,3,2,Qt.AlignCenter)
        grid.addWidget(rightLabel,3,3,Qt.AlignCenter)
        grid.addWidget(bottomLabel,3,4,Qt.AlignCenter)
        grid.addWidget(topLabel,3,5,Qt.AlignCenter)
        grid.addWidget(self.bridgename,4,1,Qt.AlignCenter)
        grid.addWidget(self.left,4,2)
        grid.addWidget(self.right,4,3)
        grid.addWidget(self.bottom,4,4)
        grid.addWidget(self.top,4,5)
        grid.addWidget(button_saver,5,5)
        grid.setSpacing(10)
        grid.setContentsMargins(10,7,10,25) # (left, top, right, bottom)
        #-------grid above---------
        box_all.addLayout(grid)
        App.setLayout(self,box_all)
        App.setMinimumSize(self,self.width,self.height)
        self.show()

    # @pyqtSlot()
    def button_1_clicked(self):
        self.file_name=QFileDialog.getOpenFileName(self,filter=self.filter)
        print(self.file_name)
        print("type(self.file_name)=",type(self.file_name))
        self.qlfname.setText(self.file_name[0])
        # file=os.read(self.file_name[0])
        # with codecs.open(self.file_name[0],'r+',encoding='utf-8') as csvfile:
        with codecs.open(self.file_name[0],'r+') as csvfile:
            headline=csvfile.readline()
            print(headline)
            print("success")

        self.fchosen=True

    def button_saver_clicked(self):
        # if(self.fchosen):
        array=[]
        array.append(self.bridgename.text())
        array.append(self.left.text())
        array.append(self.right.text())
        array.append(self.bottom.text())
        array.append(self.top.text())
        print(array)
        # print("type(array[0]) ",type(array[0]))






app=QApplication(sys.argv)
ex=App()
sys.exit(app.exec_())










