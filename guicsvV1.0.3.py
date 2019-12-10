from tkinter import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import pandas as pd
import os
import codecs
import re

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
        self.last_index=0
        self.str_header = ",bridge_name,left,right,bottom,top\n"
        self.fchosen=False
        self.header=False
        self.filter="*.csv"
        self.file_name="Choose *.CSV file"
        self.qlfname=QLabel(self.file_name)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height) #left right bottom top
        grid=QGridLayout()
        button_file_choose=QPushButton("Open file",self)
        button_file_choose.setToolTip("Are you sure about that")
        button_file_choose.move(0,0)
        button_file_choose.clicked.connect(self.button_file_choose_clicked)
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
        box_all.addWidget(button_file_choose,Qt.AlignTop | Qt.AlignLeft)
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
    def button_file_choose_clicked(self):
        self.file_name=QFileDialog.getOpenFileName(self,filter=self.filter)
        print("self.file_name[0] ",self.file_name[0])
        print(self.file_name)
        print("type(self.file_name)=",type(self.file_name))
        self.qlfname.setText(self.file_name[0])

        with codecs.open(self.file_name[0],"r") as csvfile:
            if(os.path.isfile(self.file_name[0]) and os.path.getsize(self.file_name[0])>0): # true if file isnt empty
                lines = csvfile.readlines()
                line_first=lines[0].split(",")
                line_last=lines[-1].split(",")
                print("line_first[0] ",line_first[0])
                print("line_last[0] ",line_last[0])
                if(line_first[0]=='' or line_first[0]==""):
                # if(last_line[0][0]==',' or last_line[0][0]=="," ):
                    self.header=True
                    if(line_last[0]!='' or line_last[0]!=""):
                        self.last_index=int(line_last[0])
                        self.last_index+=1
                    else:
                        self.last_index=int(0)
                else:
                    print("something goes wrong")

            else:
                self.header=False
        self.fchosen=True
        print("self.header= ",self.header)
        print("self.last_index= ",self.last_index)
        print("--------------------------------------------")
#-23,432
#Arisona    rangers *@#(@  12
    def button_saver_clicked(self):
        if(self.fchosen):
            array=[]
            left=(self.left.text()).replace(",",".")
            right=(self.right.text()).replace(",",".")
            bottom=(self.bottom.text()).replace(",",".")
            top=(self.top.text()).replace(",",".")
            bridge_name=self.bridgename.text()
            bridge_name=re.sub('[^a-zA-Z0-9]',"_",bridge_name)
            # bridge_name=bridge_name.replace('[^0-1]',"_")
            print("bridge_name ",bridge_name)
            array.append(bridge_name)
            array.append(left)
            array.append(right)
            array.append(bottom)
            array.append(top)

            with codecs.open(self.file_name[0], "a") as csvfile:
                if(not self.header):
                    csvfile.write(self.str_header)
                    self.header=True
                csvfile.write(str(self.last_index))
                self.last_index+=1
                for i in range(len(array)):
                    csvfile.write(",")
                    csvfile.write(array[i])
                csvfile.write("\n")


            print(array)
            # print("type(array[0]) ",type(array[0]))




app=QApplication(sys.argv)
ex=App()
sys.exit(app.exec_())










