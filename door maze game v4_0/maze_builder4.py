# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maze_builder4.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(955, 550)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 190, 36, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(710, 160, 36, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(671, 190, 36, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 190, 35, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(854, 100, 81, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(815, 70, 51, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(870, 70, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(670, 430, 37, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(730, 430, 51, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 20, 611, 481))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(902, 191, 35, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(850, 160, 36, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(818, 191, 36, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(860, 190, 36, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(840, 140, 81, 20))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(700, 140, 51, 20))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(670, 450, 196, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 1, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_2.addWidget(self.pushButton_13, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(800, 430, 51, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(670, 300, 81, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(670, 280, 71, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(850, 300, 81, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_5 = QtWidgets.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(670, 20, 111, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(670, 70, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(670, 50, 61, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(670, 100, 111, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(800, 10, 16, 241))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(670, 260, 251, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(670, 130, 121, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(740, 230, 61, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(670, 230, 61, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(670, 340, 171, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 0, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 1, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 1, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(760, 300, 81, 23))
        self.pushButton_20.setObjectName("pushButton_20")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_4.setText(_translate("Form", "v"))
        self.pushButton_4.setShortcut(_translate("Form", "Down"))
        self.pushButton.setText(_translate("Form", "^"))
        self.pushButton.setShortcut(_translate("Form", "Up"))
        self.pushButton_2.setText(_translate("Form", "<"))
        self.pushButton_2.setShortcut(_translate("Form", "Left"))
        self.pushButton_3.setText(_translate("Form", ">"))
        self.pushButton_3.setShortcut(_translate("Form", "Right"))
        self.pushButton_5.setText(_translate("Form", "Hide Lever"))
        self.pushButton_5.setShortcut(_translate("Form", "K"))
        self.label_3.setText(_translate("Form", "Lever ID:"))
        self.label.setText(_translate("Form", "# Rows"))
        self.label_2.setText(_translate("Form", "# Columns"))
        self.pushButton_6.setText(_translate("Form", "D"))
        self.pushButton_6.setShortcut(_translate("Form", "D"))
        self.pushButton_9.setText(_translate("Form", "W"))
        self.pushButton_9.setShortcut(_translate("Form", "W"))
        self.pushButton_17.setText(_translate("Form", "A"))
        self.pushButton_17.setShortcut(_translate("Form", "A"))
        self.pushButton_18.setText(_translate("Form", "S"))
        self.pushButton_18.setShortcut(_translate("Form", "S"))
        self.label_5.setText(_translate("Form", "Place/Lock Doors"))
        self.label_4.setText(_translate("Form", "Navigate"))
        self.comboBox_2.setItemText(0, _translate("Form", "1"))
        self.comboBox_2.setItemText(1, _translate("Form", "2"))
        self.comboBox_2.setItemText(2, _translate("Form", "3"))
        self.comboBox_2.setItemText(3, _translate("Form", "4"))
        self.comboBox_2.setItemText(4, _translate("Form", "5"))
        self.comboBox_2.setItemText(5, _translate("Form", "6"))
        self.comboBox_2.setItemText(6, _translate("Form", "7"))
        self.comboBox_3.setItemText(0, _translate("Form", "1"))
        self.comboBox_3.setItemText(1, _translate("Form", "2"))
        self.comboBox_3.setItemText(2, _translate("Form", "3"))
        self.comboBox_3.setItemText(3, _translate("Form", "4"))
        self.comboBox_3.setItemText(4, _translate("Form", "5"))
        self.comboBox_3.setItemText(5, _translate("Form", "6"))
        self.comboBox_3.setItemText(6, _translate("Form", "7"))
        self.comboBox.setItemText(0, _translate("Form", "1"))
        self.comboBox.setItemText(1, _translate("Form", "2"))
        self.pushButton_12.setText(_translate("Form", "Build"))
        self.pushButton_12.setShortcut(_translate("Form", "Ctrl+B"))
        self.pushButton_13.setText(_translate("Form", "Clear"))
        self.pushButton_13.setShortcut(_translate("Form", "Ctrl+Shift+C"))
        self.label_6.setText(_translate("Form", "# Floors"))
        self.label_7.setText(_translate("Form", "Current Floor:"))
        self.pushButton_7.setText(_translate("Form", "Add Ramp"))
        self.pushButton_7.setShortcut(_translate("Form", "R"))
        self.comboBox_5.setItemText(0, _translate("Form", "Available Cheats"))
        self.label_8.setText(_translate("Form", "Passcode:"))
        self.pushButton_19.setText(_translate("Form", "Add to Cheats"))
        self.pushButton_11.setText(_translate("Form", "Finish"))
        self.pushButton_11.setShortcut(_translate("Form", "Ctrl+Shift+F"))
        self.pushButton_10.setText(_translate("Form", "Start"))
        self.pushButton_10.setShortcut(_translate("Form", "Ctrl+Shift+S"))
        self.pushButton_8.setText(_translate("Form", "Save Cheats"))
        self.pushButton_15.setText(_translate("Form", "Save"))
        self.pushButton_15.setShortcut(_translate("Form", "Ctrl+Alt+S"))
        self.pushButton_16.setText(_translate("Form", "Load Cheats"))
        self.pushButton_14.setText(_translate("Form", "Load"))
        self.pushButton_14.setShortcut(_translate("Form", "Ctrl+Alt+O"))
        self.pushButton_20.setText(_translate("Form", "Toggle Floors"))
        self.pushButton_20.setShortcut(_translate("Form", "F"))

