
from PyQt5 import QtCore, QtGui, QtWidgets
import Dialog2 as D2
import Dialog3 as D3



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hlogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 10, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 50, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 61, 71))
        #self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setText("")

        self.pix=QtGui.QPixmap('E:/jozve/python/projects/Pyqt5/1/logo.PNG')
        self.label_3.setPixmap(self.pix)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(26, 140, 51, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 71, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(26, 220, 51, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 140, 150, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 180, 150, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 220, 150, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(290, 140, 71, 16))
        self.label_7.setObjectName("label_7")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(290, 170, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 200, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(410, 170, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(410, 140, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(370, 230, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 290, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 290, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.radioButton.toggled.connect(lambda : self.radiobutton(self.radioButton))
        self.radioButton_2.toggled.connect(lambda : self.radiobutton(self.radioButton_2))
        
        
        #d3.buttonBox.accepted.connect(lambda: dialog3.close())
        
        
        
        
    def yes(self):
        d2=D2.Ui_Dialogprint()
        dialog2=QtWidgets.QDialog()
        d2.setupUi(dialog2)
        f1=self.lineEdit.text()
        f2=self.lineEdit_2.text()
        f3=self.lineEdit_3.text()
        fr=self.current_radio
        total_price=float(self.comboBox.currentText())*100
        d2.textEdit.setText('Name:\t '+f1+'\nPhone Number:\t '+f2+'\nEmail:\t '+f3+'\nSex:\t '+fr+
                            "\nNights you'll stay: "+self.comboBox.currentText()+'\n'+'\nprice = '+str(total_price))
        #+'\n\n\nTotal Price =\t '+str(total_price))
                            
        
        print(f1+'\n'+f2+'\n'+f3)
        d2.pushButton.clicked.connect(lambda: dialog2.close())
        d2.pushButton_2.clicked.connect(lambda: self.write(f1,f2,f3,fr,total_price))
        d2.pushButton_2.clicked.connect(lambda: dialog2.close())
        d2.pushButton_2.clicked.connect(lambda: self.lineEdit.clear())
        d2.pushButton_2.clicked.connect(lambda: self.lineEdit_2.clear())
        d2.pushButton_2.clicked.connect(lambda: self.lineEdit_3.clear())
        
        dialog2.exec_()

    def write(self,f1,f2,f3,fr,total_price):
        f=self.lineEdit.text()+'.txt'
        file=open(f,'w+')
        file.write('Name:\t '+f1+'\nPhone Number:\t '+f2+'\nEmail:\t '+f3+'\nSex:\t '+fr+
                            "\nNights you'll stay: "+self.comboBox.currentText()+'\n'+'\nprice = '+str(total_price)+
                   '\n'+'Your reservation code is '+str(len(f1))+f1[0]+f1[-1]+str(len(f1)-3)+'Gl'+'\nHave a good trip!')
        file.close()
        
        
  
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Reservation Hotel"))
        self.label.setText(_translate("Form", "In the Name of God"))
        self.label_2.setText(_translate("Form", "Welcome to the Golden Hotel!"))
        self.label_4.setText(_translate("Form", "Name"))
        self.label_5.setText(_translate("Form", "Phone Number"))
        self.label_6.setText(_translate("Form", "Email"))
        self.label_7.setText(_translate("Form", "Gender:"))
        self.radioButton.setText(_translate("Form", "Male"))
        self.radioButton_2.setText(_translate("Form", "Female"))
        self.comboBox.setItemText(0, _translate("Form", "1"))
        self.comboBox.setItemText(1, _translate("Form", "2"))
        self.comboBox.setItemText(2, _translate("Form", "3"))
        self.comboBox.setItemText(3, _translate("Form", "4"))
        self.comboBox.setItemText(4, _translate("Form", "5"))
        self.label_8.setText(_translate("Form", "How many nights?"))
        self.label_9.setText(_translate("Form", "Each night\'s price is 100 $"))
        self.pushButton.setText(_translate("Form", "Reserve"))
        self.pushButton_2.setText(_translate("Form", "Clear"))
        self.pushButton_3.setText(_translate("Form", "print"))
        

        
        

    def radiobutton(self,selected):
        if selected.isChecked():
            self.current_radio=selected.text()
            print(self.current_radio)
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    
    ###=================================Dialog 3   DialogButtonBox
    d3=D3.Ui_DialogMessage()
    dialog3=QtWidgets.QDialog()
    d3.setupUi(dialog3)
    ui.pushButton.clicked.connect(lambda : dialog3.exec_())  ###Reserve Button
    d3.buttonBox.accepted.connect(lambda: ui.yes())
    d3.buttonBox.accepted.connect(lambda: dialog3.close())
    d3.buttonBox.rejected.connect(lambda: dialog3.close())
    d3.buttonBox.helpRequested.connect(lambda: print('help!'))
    d3.buttonBox.helpRequested.connect(lambda: dialog3.close())
    ###=================================Dialog 2   print
    d2=D2.Ui_Dialogprint()
    dialog2=QtWidgets.QDialog()
    d2.setupUi(dialog2)
    ###====================================== Clear Button
    ui.pushButton_2.clicked.connect(lambda: ui.lineEdit.clear())
    ui.pushButton_2.clicked.connect(lambda: ui.lineEdit_2.clear())
    ui.pushButton_2.clicked.connect(lambda: ui.lineEdit_3.clear())

    
    sys.exit(app.exec_())
    
    
    

    
