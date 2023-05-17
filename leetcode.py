from PyQt5 import QtCore, QtGui, QtWidgets
from os import system


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(3000, 1800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(0,0, 300, 100))
        self.pushButton1.clicked.connect(self.read_file1)
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(0,100, 300, 100))
        self.pushButton2.clicked.connect(self.read_file2)
        
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(0,200, 300, 100))
        self.pushButton3.clicked.connect(self.read_file3)
        
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(0,300, 300, 100))
        self.pushButton4.clicked.connect(self.read_file4)
        
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(0,2800, 100, 100))
    
        self.plainTextEdit1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit1.setGeometry(QtCore.QRect(300, 0, 1000, 1800))

        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit2.setGeometry(QtCore.QRect(1300, 0, 2000, 900))
        
        self.plainTextEdit3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit3.setGeometry(QtCore.QRect(1300, 900, 2000, 900))
        
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(3300,0, 150, 100))
        self.pushButton5.clicked.connect(self.run)
         
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton1.setText(_translate("MainWindow", "Merge Sorted Array"))
        self.pushButton2.setText(_translate("MainWindow", "Majority Element"))
        self.pushButton3.setText(_translate("MainWindow", "Contains Duplicate"))
        self.pushButton4.setText(_translate("MainWindow", "Missing Number"))
        self.pushButton5.setText(_translate("MainWindow", "RUN"))

    def read_file1(self):
        s = ''
        with open("MergeSortedArray.txt",'r') as f:
            for sentence in f:
                s += sentence
            self.plainTextEdit1.setPlainText(s)
            self.plainTextEdit2.setPlainText("class Solution: \n\tdef solution(self, nums1, m, nums2, n):")

    def read_file2(self):
        s = ''
        with open("MajorityElement.txt",'r') as f:
            for sentence in f:
                s += sentence
            self.plainTextEdit1.setPlainText(s)
            self.plainTextEdit2.setPlainText("class Solution:\n\tdef solution(self, nums: List[int]) -> int:")
    
    def read_file3(self):
        s = ''
        with open("ContainsDuplicate.txt",'r') as f:
            for sentence in f:
                s += sentence
            self.plainTextEdit1.setPlainText(s)
            self.plainTextEdit2.setPlainText("class Solution:\n\tdef solution(self, nums: List[int]) -> bool:")

    def read_file4(self):
        ...
        s = ''
        with open("MissingNumber.txt",'r') as f:
            for sentence in f:
                s += sentence
            self.plainTextEdit1.setPlainText(s)
            self.plainTextEdit2.setPlainText("class Solution:\n\tdef solution(self, nums: List[int]) -> int:")
    
    def run(self):
        with open("foo.py","w") as f:
            f.write(self.plainTextEdit2.toPlainText())
            f.write("\nm = Solution()\ns = m.solution([1,2,3,0,0,0],3,nums2 = [2,5,6], n = 3)\nwith open('foo2.txt','w') as f:\n\tf.write(s)")
        system("python3 foo.py")   
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
