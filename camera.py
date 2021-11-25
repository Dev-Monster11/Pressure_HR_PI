
from PyQt5.QtCore import QObject, QThread
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap
from blurring import face_simple, face_pixelate 
import face_recognition
import os
import cv2
class CameraBackend(QObject):
    def __init__(self):
        super(CameraBackend, self).__init__()
        self.tempPath = './'
    def setViewFinder(self, label):
        self.viewFinder = label
    def startStreaming(self):
        self.index = 0
        self.cap = cv2.VideoCapture(0)
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.captureVideo)
        self.thread.start()
    def setTempPath(self, tmpPath):
        self.tempPath = tmpPath
    def stopStream(self):
        pass
    def captureVideo(self):
        if not self.cap.isOpened():
            return
        if os.path.exists(self.tempPath):
            os.chdir(self.tempPath)
        while True:
            _, frame = self.cap.read()
            self.index += 1
            image = frame.copy()
            
            face_location = face_recognition.face_locations(image)
            
            if (len(face_location) > 0):
                (top, right, bottom, left) = face_location[0]
                face_image = image[top:bottom, left:right]
                face_image = face_pixelate(face_image, 5)
                image[top:bottom, left:right] = face_image
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            cv2.imwrite("{1}.jpg", image)
            h, w = image.shape

            bPL = w
            qImg = QImage(image.data, w, h, bPL, QImage.Format_Mono)
            self.viewFinder.setPixmap(QPixmap.fromImage(qImg))
            
            QThread.msleep(40)
    
