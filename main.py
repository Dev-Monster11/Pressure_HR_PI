
import sys


from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF, QMargins, QTimer
from PyQt5.QtGui import QPainter
from ui import Ui_Dialog
from camera import CameraBackend
from db import DataBackend
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


        #---Connection
        self.ui.btnStart.clicked.connect(self.btnStart_clicked)
        self.ui.btnExit.clicked.connect(self.btnExit_clicked)



        self.camera.setViewFinder(self.ui.label)
    def btnExit_clicked(self):
        sys.exit(0)
    def btnStart_clicked(self):
        self.startFlag = not self.startFlag
        if self.startFlag == True:
            self.ui.btnStart.setText('Start')
        else:
            self.ui.btnStart.setText('Stop')
            self.camera.startStreaming()

def main():
    app = QApplication(sys.argv)
    maindlg = MainDlg()
    # window = QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(window)
    # layout(window, ui)
    # processChart(ui)
    # processConnect(ui)
    maindlg.showFullScreen()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()