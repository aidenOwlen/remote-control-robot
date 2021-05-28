# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\blackytner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1303, 849)
        MainWindow.setStyleSheet(_fromUtf8("background:black;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.joystick = QtGui.QTabWidget(self.centralwidget)
        self.joystick.setGeometry(QtCore.QRect(0, 0, 1321, 801))
        self.joystick.setStyleSheet(_fromUtf8("background:black;\n"
"font:bold;\n"
""))
        self.joystick.setObjectName(_fromUtf8("joystick"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(1110, 20, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 131, 21))
        self.label_2.setStyleSheet(_fromUtf8("color:white;\n"
"font: 75 12pt  \"Unispace\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_2 = QtGui.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(710, 0, 21, 771))
        self.line_2.setStyleSheet(_fromUtf8("background:white;"))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton_5 = QtGui.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 700, 93, 28))
        self.pushButton_5.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(730, 150, 571, 20))
        self.line.setStyleSheet(_fromUtf8("background:white;"))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(920, 700, 93, 28))
        self.pushButton_6.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(1030, 700, 93, 28))
        self.pushButton_7.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(750, 200, 231, 151))
        self.groupBox.setStyleSheet(_fromUtf8("color:white;"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.off = QtGui.QPushButton(self.groupBox)
        self.off.setGeometry(QtCore.QRect(110, 90, 93, 28))
        self.off.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.off.setObjectName(_fromUtf8("off"))
        self.on = QtGui.QPushButton(self.groupBox)
        self.on.setGeometry(QtCore.QRect(110, 40, 93, 28))
        self.on.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.on.setObjectName(_fromUtf8("on"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(1030, 200, 231, 151))
        self.groupBox_2.setStyleSheet(_fromUtf8("color:white;"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 30, 31, 16))
        self.label_9.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_10.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 113, 22))
        self.lineEdit.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 113, 22))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.updateLogs = QtGui.QPushButton(self.groupBox_2)
        self.updateLogs.setGeometry(QtCore.QRect(100, 110, 111, 28))
        self.updateLogs.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.updateLogs.setObjectName(_fromUtf8("updateLogs"))
        self.pushButton_10 = QtGui.QPushButton(self.tab)
        self.pushButton_10.setGeometry(QtCore.QRect(1140, 700, 93, 28))
        self.pushButton_10.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(940, 50, 151, 41))
        self.label_11.setStyleSheet(_fromUtf8("color:rgb(152, 0, 0);\n"
"font: 75 14pt  \"Unispace\";"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.state = QtGui.QLabel(self.tab)
        self.state.setGeometry(QtCore.QRect(20, 740, 141, 16))
        self.state.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.state.setObjectName(_fromUtf8("state"))
        self.joystick_2 = QtGui.QGroupBox(self.tab)
        self.joystick_2.setGeometry(QtCore.QRect(230, 570, 231, 151))
        self.joystick_2.setObjectName(_fromUtf8("joystick_2"))
        self.start = QtGui.QPushButton(self.tab)
        self.start.setGeometry(QtCore.QRect(232, 730, 231, 28))
        self.start.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.start.setObjectName(_fromUtf8("start"))
        self.autoSpeak = QtGui.QGroupBox(self.tab)
        self.autoSpeak.setGeometry(QtCore.QRect(750, 370, 511, 91))
        self.autoSpeak.setStyleSheet(_fromUtf8("color:white;"))
        self.autoSpeak.setObjectName(_fromUtf8("autoSpeak"))
        self.auto_2 = QtGui.QPushButton(self.autoSpeak)
        self.auto_2.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.auto_2.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.auto_2.setObjectName(_fromUtf8("auto_2"))
        self.label_13 = QtGui.QLabel(self.autoSpeak)
        self.label_13.setGeometry(QtCore.QRect(280, 40, 41, 16))
        self.label_13.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.min = QtGui.QLineEdit(self.autoSpeak)
        self.min.setGeometry(QtCore.QRect(330, 40, 51, 22))
        self.min.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.min.setObjectName(_fromUtf8("min"))
        self.max = QtGui.QLineEdit(self.autoSpeak)
        self.max.setGeometry(QtCore.QRect(420, 40, 51, 22))
        self.max.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.max.setObjectName(_fromUtf8("max"))
        self.label_14 = QtGui.QLabel(self.autoSpeak)
        self.label_14.setGeometry(QtCore.QRect(390, 40, 31, 16))
        self.label_14.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.custom = QtGui.QGroupBox(self.tab)
        self.custom.setGeometry(QtCore.QRect(750, 480, 511, 151))
        self.custom.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.custom.setObjectName(_fromUtf8("custom"))
        self.label_12 = QtGui.QLabel(self.custom)
        self.label_12.setGeometry(QtCore.QRect(170, 50, 211, 16))
        self.label_12.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.speakk = QtGui.QLineEdit(self.custom)
        self.speakk.setGeometry(QtCore.QRect(40, 90, 441, 31))
        self.speakk.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"color:white;"))
        self.speakk.setObjectName(_fromUtf8("speakk"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 671, 481))
        self.label_3.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.joystick.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.joystick.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1303, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.joystick.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Blackytner", None))
        self.label.setText(_translate("MainWindow", "State : Connected", None))
        self.label_2.setText(_translate("MainWindow", "Cam view", None))
        self.pushButton_5.setText(_translate("MainWindow", "Reboot", None))
        self.pushButton_6.setText(_translate("MainWindow", "Shutdown", None))
        self.pushButton_7.setText(_translate("MainWindow", "Disconnect", None))
        self.groupBox.setTitle(_translate("MainWindow", "LED", None))
        self.off.setText(_translate("MainWindow", "Off", None))
        self.on.setText(_translate("MainWindow", "On", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Change wifi logs", None))
        self.label_9.setText(_translate("MainWindow", "ssid :", None))
        self.label_10.setText(_translate("MainWindow", "password:", None))
        self.updateLogs.setText(_translate("MainWindow", "Update logs", None))
        self.pushButton_10.setText(_translate("MainWindow", "Deep sleep ", None))
        self.label_11.setText(_translate("MainWindow", "Blackytner", None))
        self.state.setText(_translate("MainWindow", "State : Connected", None))
        self.joystick_2.setTitle(_translate("MainWindow", "GroupBox", None))
        self.start.setText(_translate("MainWindow", "Start", None))
        self.autoSpeak.setTitle(_translate("MainWindow", "Automatic speak", None))
        self.auto_2.setText(_translate("MainWindow", "On", None))
        self.label_13.setText(_translate("MainWindow", "Rate :", None))
        self.label_14.setText(_translate("MainWindow", "To :", None))
        self.custom.setTitle(_translate("MainWindow", "Custom message", None))
        self.label_12.setText(_translate("MainWindow", "Hello, I am trying to speak !!", None))
        self.joystick.setTabText(self.joystick.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.joystick.setTabText(self.joystick.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

