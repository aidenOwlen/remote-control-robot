# -*- coding:utf-8 -*-
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from PyQt4.QtCore import QThread 
from PyQt4 import QtCore, QtGui 
from blackytner import *
import urllib.request
from threading import Thread 
from PyQt4.QtWebKit import QWebView,QWebSettings
import time
import socket 
from enum import Enum
import random
import cv2

global Dir 
Dir = b"Default"
writing = False
AUTO = True

class videoThread(QThread):

    def __init__(self,address):
        super(videoThread,self).__init__()
        self.ip = address

    def run(self):
        cap = cv2.VideoCapture("http://"+ str(self.ip) + ":81/stream")
        while cap.isOpened():
            _,frame = cap.read()
            # adjust width en height to the preferred values
            image = QImage(frame.tostring(),640,480,QImage.Format_GRAYSCALE)
            image.rgbSwapped() 
            self.emit(SIGNAL('newImage(QImage)'), image)

class sendingVoice(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.listVoico = ["Hello Cat","Hello Ai","testing Stuff","Random shit"]
    def run(self):
        global AUTO
        while 1:

            self.voiceToSend = random.choice(self.listVoico)
            self.voiceToSend = self.voiceToSend.replace(" ","$")

            try:
                if AUTO == True:
                    urllib.request.urlopen("http://www.blackytner.tech/catPhpWork.php?speak={}".format(self.voiceToSend))
                    print(self.voiceToSend)
                    time.sleep(random.randint(5,35))
                else:
                    pass

            except Exception as J:
                print(J)


class writingDir(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect(("www.blackytner.tech",80))
        self.dir = "mac"
    def run(self):
        
        i = 0
        global Dir
        while writing:
            
                
                try:
                    if self.dir != Dir:
                        
                        self.s.sendall(b"GET /direction.php?dir="+ Dir+b" HTTP/1.1\r\nHost: www.blackytner.tech\r\n\r\n") 
                        self.dir = Dir
                        print(self.dir)
                    
                except:
                    i+= 1
                    if i>= 100:
                        self.s.close()
                        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                        self.s.connect(("www.blackytner.tech",80))
                        
                        i = 0
            



class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Joystick(QWidget):
    def __init__(self, parent=None):
        global Dir
        super(Joystick, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.movingOffset = QPointF(0, 0)
        self.grabCenter = False
        self.__maxDistance = 50

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.black)
        bounds = QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2, self.__maxDistance * 2).translated(self._center())

        painter.drawEllipse(bounds)
        painter.setBrush(Qt.red)

        painter.drawEllipse(self._centerEllipse())

    def _centerEllipse(self):
        if self.grabCenter:
            return QRectF(-20, -20, 40, 40).translated(self.movingOffset)
        return QRectF(-20, -20, 40, 40).translated(self._center())

    def _center(self):
        return QPointF(self.width()/2, self.height()/2)


    def _boundJoystick(self, point):
        limitLine = QLineF(self._center(), point)
        if (limitLine.length() > self.__maxDistance):
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()

    def joystickDirection(self):
        global Dir

        if not self.grabCenter:
            return 0
        normVector = QLineF(self._center(), self.movingOffset)
        currentDistance = normVector.length()
        angle = normVector.angle()

        distance = min(currentDistance / self.__maxDistance, 1.0)
        if 107 <= angle < 175:
            Dir = b"LeftUp"
        elif 0 <= angle < 65:
            Dir = b"RightUp"

        elif 65 <= angle < 175:
            Dir = b"UP"
        elif 107 <= angle < 252:
            Dir = b"LeftDown"
        elif 288 <= angle < 359:
            Dir = b"RightDown"
        elif 252 <= angle < 288:
            Dir = b"DOWN"
        else:
            Dir = b"Zero"
        return Dir

        """

        if 45 <= angle < 135:
            return ("UP", distance)
        elif 135 <= angle < 225:
            return (Direction.Left, distance)
        elif 225 <= angle < 315:
            return (Direction.Down, distance)
        return (Direction.Right, distance)
        """
        


    def mousePressEvent(self, ev):
      
        self.grabCenter = self._centerEllipse().contains(ev.pos())
        return super().mousePressEvent(ev)

    def mouseReleaseEvent(self, event):
        global Dir
        
        self.grabCenter = False
        self.movingOffset = QPointF(0, 0)
        self.update()
        Dir = b"Zero"
       

    def mouseMoveEvent(self, event):
     
        
        if self.grabCenter:
        
            self.movingOffset = self._boundJoystick(event.pos())
           
            self.update()
            
        Dir = self.joystickDirection()



  

class myInterface(Ui_MainWindow):
    def retranslateUi(self,MainWindow):
        super(__class__,self).retranslateUi(MainWindow)
       

        

        self.on.clicked.connect(self.ON)
        self.off.clicked.connect(self.OFF)
    
      
        self.state = "J"
        joystick = Joystick(self.joystick_2)
        joystick.setGeometry(60,23,5,5)
        self.joystick_2.setStyleSheet("border:2px solid White;color:white")
        self.joystick_2.setTitle("Joystick")
        self.start.clicked.connect(self.startt)
        self.updateLogs.clicked.connect(self.updatelogs)
        self.speakk.returnPressed.connect(self.speakit)
        self.auto_2.setText("Off")
        self.auto_2.clicked.connect(self.AutoOff)
        self.custom.setVisible(False)
        self.min.setText("5")
        self.max.setText("38")
        self.pushButton_5.clicked.connect(self.reboot)
        self.pushButton_6.clicked.connect(self.shutIt)
        self.video = videoThread("192.168.43.194")
        self.video.start()
        #my label is named label
        self.label_3.connect(self.video,SIGNAL('newImage(QImage)'),self.setFrame)

    def setFrame(self,frame):
        pixmap = QPixmap.fromImage(frame)
        self.label_3.setPixmap(pixmap)
    def shutIt(self):
        urllib.request.urlopen("http://www.blackytner.tech/catPhpWork.php?deepSleepXX*36000000")
    def reboot(self):
        urllib.request.urlopen("http://www.blackytner.tech/catPhpWork.php?deepSleepXX*1")

    def AutoOff(self):
        global AUTO
        if self.auto_2.text() == "Off":
            AUTO = False
            self.auto_2.setText("On")
            self.custom.setVisible(True)
        else:
            AUTO = True
            self.auto_2.setText("Off")
            self.custom.setVisible(False)

    def speakit(self):
        self.textoo = self.speakk.text().replace(" ", "$")
        urllib.request.urlopen("http://www.blackytner.tech/catPhpWork.php?speak={}".format(self.textoo))
        self.speakk.setText("")
    def updatelogs(self):
        urllib.request.urlopen("http://www.blackytner.tech/logs.php?ssid={}&password={}".format(self.lineEdit.text(),self.lineEdit_2.text()))
        urllib.request.urlopen("http://www.blackytner.tech/direction.php?dir=ChangeLog")
    def startt(self):
        print("Starting")
        global writing
        if self.start.text() == "Start":
            writing = True
            self.loop1 = writingDir()
            self.loop1.start()
            self.start.setText("Stop")
        else:
            writing = False
            self.start.setText("Start")

    def ON(self):
         urllib.request.urlopen('https://www.pequea.net/testo.php?q=H')
    def OFF(self):
        urllib.request.urlopen('https://www.pequea.net/testo.php?q=J')
if __name__ == "__main__":
    import sys 
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = myInterface()
    ui.setupUi(MainWindow)
    

    # Create joystick 
    

    # ml.addLayout(joystick.get_joystick_layout(),0,0)
  

    sendingvoice = sendingVoice()
    sendingvoice.start()
    MainWindow.show()
    sys.exit(app.exec_())

