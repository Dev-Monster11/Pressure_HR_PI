from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
import pexpect

class Pressure(QObject):
    def __init__(self):
        super(Pressure, self).__init__()
        self.retry = True
    def startPressure(self):
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.capturePressure)
        self.thread.start()