# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1909, 988)
        Dialog.setStyleSheet("QWidget{\n"
"    font-size: 30px;\n"
"}\n"
"QDialog {\n"
"    background-color:rgb(82, 82, 82);\n"
"}\n"
"QTextEdit {\n"
"    background-color:rgb(42, 42, 42);\n"
"    color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"    border-bottom-color: rgb(115, 115, 115);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"    border-style: solid;\n"
"    color: rgb(0, 0, 0);\n"
"    padding: 2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}\n"
"QLineEdit {\n"
"    border-width: 1px; border-radius: 4px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    padding: 0 8px;\n"
"    color: rgb(255, 255, 255);\n"
"    background:rgb(100, 100, 100);\n"
"    selection-background-color: rgb(187, 187, 187);\n"
"    selection-color: rgb(60, 63, 65);\n"
"}\n"
"QLabel {\n"
"    color:rgb(255,255,255);    \n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color:rgb(77,77,77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"    border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"    background:rgb(82, 82, 82);\n"
"}\n"
"QMenuBar::item {\n"
"    color:rgb(223,219,210);\n"
"    spacing: 3px;\n"
"    padding: 1px 4px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background:rgb(115, 115, 115);\n"
"}\n"
"QMenu::item:selected {\n"
"    color:rgb(255,255,255);\n"
"    border-width:2px;\n"
"    border-style:solid;\n"
"    padding-left:18px;\n"
"    padding-right:8px;\n"
"    padding-top:2px;\n"
"    padding-bottom:3px;\n"
"    background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"    border-bottom-color: rgb(58, 58, 58);\n"
"    border-bottom-width: 1px;\n"
"}\n"
"QMenu::item {\n"
"    color:rgb(223,219,210);\n"
"    background-color:rgb(78,78,78);\n"
"    padding-left:20px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:10px;\n"
"}\n"
"QMenu{\n"
"    background-color:rgb(78,78,78);\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(77,77,77);\n"
"        background-color:rgb(101,101,101);\n"
"        border-style: solid;\n"
"        border-width: 1px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab {\n"
"    padding:2px;\n"
"    color:rgb(250,250,250);\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"      border-top-right-radius:4px;\n"
"   border-top-left-radius:4px;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"    border-bottom-color: rgb(101,101,101);\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      background-color:rgb(101,101,101);\n"
"      margin-left: 0px;\n"
"      margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"        margin-top: 1px;\n"
"        margin-right: 1px;\n"
"}\n"
"QCheckBox {\n"
"    color:rgb(223,219,210);\n"
"    padding: 2px;\n"
"}\n"
"QCheckBox:hover {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    padding-left: 1px;\n"
"    padding-right: 1px;\n"
"    padding-bottom: 1px;\n"
"    padding-top: 1px;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(180,180,180);\n"
"      background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-radius:4px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgb(87, 97, 106);\n"
"      background-color:rgb(255,255,255);\n"
"}\n"
"QStatusBar {\n"
"    color:rgb(240,240,240);\n"
"}\n"
"QGroupBox{\n"
"    border-radius: 10px;\n"
"    border: 1px solid white;\n"
"}\n"
"QListWidget{\n"
"    border: 1px solid gray;\n"
"}")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1011, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.realtimeLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.realtimeLayout.setContentsMargins(10, 10, 10, 10)
        self.realtimeLayout.setObjectName("realtimeLayout")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.realtimeLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.realtimeLayout.addWidget(self.label, 0, 0, 1, 1)
        self.hrLayout = QtWidgets.QHBoxLayout()
        self.hrLayout.setContentsMargins(10, 10, 10, 10)
        self.hrLayout.setObjectName("hrLayout")
        self.realtimeLayout.addLayout(self.hrLayout, 0, 1, 1, 1)
        self.realtimeLayout.setColumnStretch(0, 1)
        self.realtimeLayout.setColumnStretch(1, 1)
        self.realtimeLayout.setRowStretch(0, 10)
        self.realtimeLayout.setRowStretch(1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1060, 530, 401, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.groupboxLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.groupboxLayout.setContentsMargins(10, 10, 10, 0)
        self.groupboxLayout.setObjectName("groupboxLayout")
        self.btnStart = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnStart.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnStart.setObjectName("btnStart")
        self.groupboxLayout.addWidget(self.btnStart, 0, 0, 1, 1)
        self.btnExit = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnExit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnExit.setObjectName("btnExit")
        self.groupboxLayout.addWidget(self.btnExit, 0, 2, 1, 1)
        self.btnUpload = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.btnUpload.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnUpload.setObjectName("btnUpload")
        self.groupboxLayout.addWidget(self.btnUpload, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(950, 700, 391, 199))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.historyLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.historyLayout.setContentsMargins(10, 10, 10, 10)
        self.historyLayout.setObjectName("historyLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.historyLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.historyLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget_3)
        self.listWidget.setObjectName("listWidget")
        self.historyLayout.addWidget(self.listWidget, 1, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.historyLayout.addWidget(self.groupBox_2, 2, 0, 1, 2)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(160, 500, 611, 361))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.mainLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setObjectName("mainLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.mainLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size: 40px;\n"
"font-weight: bold;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.mainLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(1320, 380, 561, 80))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout.setContentsMargins(50, 0, 50, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnStart_2 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.btnStart_2.setMinimumSize(QtCore.QSize(55, 0))
        self.btnStart_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnStart_2.setObjectName("btnStart_2")
        self.gridLayout.addWidget(self.btnStart_2, 0, 0, 1, 1)
        self.btnStart_4 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.btnStart_4.setMinimumSize(QtCore.QSize(55, 0))
        self.btnStart_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnStart_4.setObjectName("btnStart_4")
        self.gridLayout.addWidget(self.btnStart_4, 0, 2, 1, 1)
        self.btnStart_3 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.btnStart_3.setMinimumSize(QtCore.QSize(55, 0))
        self.btnStart_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnStart_3.setObjectName("btnStart_3")
        self.gridLayout.addWidget(self.btnStart_3, 0, 1, 1, 1)
        self.btnStart_5 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.btnStart_5.setMinimumSize(QtCore.QSize(55, 0))
        self.btnStart_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnStart_5.setObjectName("btnStart_5")
        self.gridLayout.addWidget(self.btnStart_5, 0, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.lblHR = QtWidgets.QLabel(Dialog)
        self.lblHR.setGeometry(QtCore.QRect(1060, 30, 131, 191))
        self.lblHR.setMinimumSize(QtCore.QSize(100, 0))
        self.lblHR.setStyleSheet("font-weight: bold;\n"
"font-size: 50px;")
        self.lblHR.setObjectName("lblHR")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnStart.setText(_translate("Dialog", "New "))
        self.btnExit.setText(_translate("Dialog", "Exit"))
        self.btnUpload.setText(_translate("Dialog", "Upload"))
        self.label_3.setText(_translate("Dialog", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "RealTime"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "History"))
        self.label_2.setText(_translate("Dialog", "Title"))
        self.btnStart_2.setText(_translate("Dialog", "<<"))
        self.btnStart_4.setText(_translate("Dialog", ">"))
        self.btnStart_3.setText(_translate("Dialog", "<"))
        self.btnStart_5.setText(_translate("Dialog", ">>"))
        self.label_4.setText(_translate("Dialog", "Page"))
        self.lblHR.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
