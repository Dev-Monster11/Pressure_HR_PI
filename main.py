
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF, QMargins
from ui import Ui_Dialog
def layout(dlg, ui):
    dlg.setLayout(ui.mainLayout)
    ui.tab.setLayout(ui.realtimeLayout)
    ui.tab_2.setLayout(ui.historyLayout)
    ui.groupBox.setLayout(ui.groupboxLayout)
    ui.groupBox_2.setLayout(ui.gridLayout)
def processChart(ui):
    series = QLineSeries()
    series.append(0, 6)
    series.append(3, 5)
    series.append(3,8)
    series.append(7,3)
    series.append(12,7)    
    chart = QChart()
    chart.addSeries(series)
    # chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.setMargins(QMargins(0, 0, 0, 0))
    chart.setTheme(QChart.ChartThemeDark)
    chartview = QChartView(chart)
    # chartview.setMargins(QMargins(0, 0, 0, 0))
    ui.realtimeLayout.addWidget(chartview, 0, 1, 1, 1)
    
    
def main():
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)
    layout(window, ui)
    processChart(ui)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__"    :
    main()