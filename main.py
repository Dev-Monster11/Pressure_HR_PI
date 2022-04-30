
import sys

import qtawesome as qta
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis, QLegend, QScatterSeries
from PyQt5.QtCore import QPointF, QMargins, QTimer, QSize, pyqtSlot, Qt
from PyQt5.QtGui import QPainter
# from maindlg import Ui_Dialog
from main_ui import Ui_MainDlg
from newdlg import Ui_NewDlg
from camera import CameraBackend
from db import DataBackend
# from hr import HeartRate
class MainDlg(QDialog):
    
    def __init__(self):
        super(MainDlg, self).__init__()
        self.newDlg = QDialog(self)
        self.newUI = Ui_NewDlg()
        self.newUI.setupUi(self.newDlg)
        self.newDlg.setLayout(self.newUI.mainLayout)
        self.newUI.btnOK.setIcon(qta.icon('fa5s.check', color="#8BC34A"))
        self.newUI.btnOK.setIconSize(QSize(48, 48))
        
        self.newUI.btnCancel.setIcon(qta.icon('fa5s.times', color="#8BC34A"))
        self.newUI.btnCancel.setIconSize(QSize(48, 48))
        #-----Layout---
        self.ui = Ui_MainDlg()
        self.ui.setupUi(self)
        self.setLayout(self.ui.mainLayout)
        self.ui.tab.setLayout(self.ui.historyLayout)
        self.ui.tab_2.setLayout(self.ui.liveLayout)
        
        self.ui.groupBox.setLayout(self.ui.actionLayout)
        self.ui.btnStart.hide()
        self.ui.btnExit_2.hide()
        self.ui.btnBlur.hide()
        #-----UI----
        self.ui.btnStart.setIcon(qta.icon('fa5s.plus', color='#8BC34A'))
        self.ui.btnStart.setIconSize(QSize(48, 48))

        self.ui.btnUpload.setIcon(qta.icon('fa5s.upload', color='#8BC34A'))
        self.ui.btnUpload.setIconSize(QSize(48, 48))

        self.ui.btnExit_1.setIcon(qta.icon('fa5s.times', color='#8BC34A'))
        self.ui.btnExit_1.setIconSize(QSize(48, 48))
        self.ui.btnExit_2.setIcon(qta.icon('fa5s.times', color='#8BC34A'))
        self.ui.btnExit_2.setIconSize(QSize(48, 48))

        #----Chart Initialization
        self.series = QLineSeries()
        self.sseries = QScatterSeries()
        self.sseries.setMarkerSize(3)
        self.sseries.setMarkerShape(QScatterSeries.MarkerShapeCircle)

        self.chart = QChart()
        
        self.axisY = QValueAxis()
        self.axisY.setRange(0, 200)
        self.axisX = QValueAxis()
        self.axisX.setRange(0, 50)
        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        self.chart.legend().setMarkerShape(QLegend.MarkerShapeCircle)
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.sseries)
        self.series.attachAxis(self.axisX)
        self.series.attachAxis(self.axisY)
        self.sseries.attachAxis(self.axisX)
        self.sseries.attachAxis(self.axisY)

        # chart.createDefaultAxes()
        self.chart.setMargins(QMargins(0, 0, 0, 0))
        self.chart.setTheme(QChart.ChartThemeDark)
        chartview = QChartView(self.chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        # self.ui.realtimeLayout.addWidget(chartview, 0, 1, 1, 1)
        self.ui.chartLayout.addWidget(chartview)
        # self.ui.chartLayout.addWidget(self.ui.lblHR)
        #---Status Variable Initialization
        self.startFlag = False
        self.camera = CameraBackend()
        self.db = DataBackend()
        # self.hr = HeartRate()

        #---Connection
        self.ui.btnNew.clicked.connect(self.btnNew_clicked)
        self.ui.btnStart.clicked.connect(self.btnStart_clicked)
        self.ui.btnExit_1.clicked.connect(self.btnExit_clicked)
        self.ui.btnExit_2.clicked.connect(self.btnExit_clicked)
        self.ui.tabWidget.currentChanged.connect(self.tabChanged)

        self.camera.setViewFinder(self.ui.label)
        # self.hr.connect()

        
        #-----global variables---
        self.index = 0
    #     self.timer = QTimer()
    #     self.timer.timeout.connect(self.abc)
    #     self.timer.start(100)
    # def abc(self):
    #     self.index += 1
    #     self.series.append(self.index, 100 - self.index)
    #     print('timereim')

    @pyqtSlot(int)
    def tabChanged(self, tabIndex):
        if tabIndex == 0:
            self.ui.btnStart.hide()
            self.ui.btnExit_2.hide()
            self.ui.btnBlur.hide()
            self.ui.btnNew.show()
            self.ui.btnExit_1.show()
            self.ui.btnUpload.show()
        else:
            self.ui.btnStart.show()
            self.ui.btnExit_2.show()
            self.ui.btnBlur.show()
            self.ui.btnNew.hide()
            self.ui.btnExit_1.hide()
            self.ui.btnUpload.hide()        
    @pyqtSlot(int)
    def HRpacketCaptured(self, hr):
        self.index += 1
        self.series.append(self.index, hr)
        self.sseries.append(self.index, hr)
        if self.index > 40:
            self.axisX.setRange(self.index - 40 + 1, self.index - 40 + 51)
        self.ui.lblHR.setText(str(hr))
        # self.index += 1
        # self.series.append(self.index, (100 - self.index) % 150)
        # print(self.index, hr)

    def btnExit_clicked(self):
        sys.exit(0)

    def btnNew_clicked(self):

        self.newDlg.exec()
    def btnStart_clicked(self):

        
        
        if self.startFlag == False:
            self.ui.btnStart.setText('Start')
            print("Stopped")
            # self.hr.stopHR()
        else:
            self.index = 0
            # self.hr.HRpacketCapture.connect(self.HRpacketCaptured)
            print("Started")
            self.ui.btnStart.setText('Stop')
            # self.hr.startHR()
            self.camera.startStreaming()
        self.startFlag = not self.startFlag            

def main():
    app = QApplication(sys.argv)
    maindlg = MainDlg()
    maindlg.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()