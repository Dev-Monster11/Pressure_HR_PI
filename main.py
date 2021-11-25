
import sys

import qtawesome as qta
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF, QMargins, QTimer, QSize, pyqtSlot
from PyQt5.QtGui import QPainter
from ui import Ui_Dialog
from camera import CameraBackend
from db import DataBackend
from hr import HeartRate
class MainDlg(QDialog):
    
    def __init__(self):
        super(MainDlg, self).__init__()

        #-----Layout---
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setLayout(self.ui.mainLayout)
        self.ui.tab.setLayout(self.ui.realtimeLayout)
        self.ui.tab_2.setLayout(self.ui.historyLayout)
        self.ui.groupBox.setLayout(self.ui.groupboxLayout)
        self.ui.groupBox_2.setLayout(self.ui.gridLayout)
        #-----UI----
        self.ui.btnStart.setIcon(qta.icon('ri.play-fill', color='#009688'))
        self.ui.btnStart.setIconSize(QSize(32, 32))

        self.ui.btnUpload.setIcon(qta.icon('ri.video-upload-fill', color='green'))
        self.ui.btnUpload.setIconSize(QSize(32, 32))

        self.ui.btnExit.setIcon(qta.icon('ri.close-circle-fill', color='green'))
        self.ui.btnExit.setIconSize(QSize(32, 32))
        #----Chart Initialization
        self.series = QLineSeries()
        chart = QChart()
        chart.addSeries(self.series)
        chart.createDefaultAxes()
        chart.setMargins(QMargins(0, 0, 0, 0))
        chart.setTheme(QChart.ChartThemeDark)
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.ui.realtimeLayout.addWidget(chartview, 0, 1, 1, 1)


        #---Status Variable Initialization
        self.startFlag = True
        self.camera = CameraBackend()
        self.db = DataBackend()
        self.hr = HeartRate()

        #---Connection
        self.ui.btnStart.clicked.connect(self.btnStart_clicked)
        self.ui.btnExit.clicked.connect(self.btnExit_clicked)



        self.camera.setViewFinder(self.ui.label)
        self.hr.connect()

        
        #-----global variables---
        self.index = 0
    @pyqtSlot(int)
    def HRpacketCaptured(self, hr):
        self.index += 1
        self.series.append(index, hr)

    def btnExit_clicked(self):
        sys.exit(0)
    def btnStart_clicked(self):

        
        self.startFlag = not self.startFlag
        if self.startFlag == True:
            self.ui.btnStart.setText('Start')
            self.hr.stopHR()
        else:
            self.index = 0
            self.hr.HRpacketCapture.connect(self.HRpacketCaptured)
            self.ui.btnStart.setText('Stop')
            self.hr.startHR()
            self.camera.startStreaming()

def main():
    app = QApplication(sys.argv)
    maindlg = MainDlg()
    maindlg.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()