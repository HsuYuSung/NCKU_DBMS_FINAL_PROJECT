# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 40, 371, 241))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(29, 285, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(419, 29, 361, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 184, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(12, 158, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(80, 156, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(12, 195, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 193, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(12, 12, 60, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(12, 45, 60, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 43, 113, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_8.setGeometry(QtCore.QRect(80, 10, 113, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(12, 82, 60, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 80, 113, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(231, 70, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(-3, 100, 361, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_19.setGeometry(QtCore.QRect(80, 120, 113, 21))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(12, 122, 60, 16))
        self.label_21.setObjectName("label_21")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(16, 72, 60, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(82, 70, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(227, 92, 121, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(16, 191, 60, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(82, 189, 113, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(227, 180, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(82, 20, 113, 21))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(2, 20, 81, 20))
        self.label_22.setObjectName("label_22")
        self.line_4 = QtWidgets.QFrame(self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(-3, 167, 361, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(17, 103, 60, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(82, 103, 113, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.line_5 = QtWidgets.QFrame(self.tab_2)
        self.line_5.setGeometry(QtCore.QRect(0, 50, 361, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.tab_2)
        self.line_6.setGeometry(QtCore.QRect(0, 126, 361, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(17, 148, 60, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(82, 148, 113, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(227, 137, 121, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(228, 149, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(18, 92, 60, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(92, 89, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_34 = QtWidgets.QLabel(self.tab_3)
        self.label_34.setGeometry(QtCore.QRect(9, 20, 81, 20))
        self.label_34.setObjectName("label_34")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_32.setGeometry(QtCore.QRect(92, 20, 113, 21))
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(227, 82, 121, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.line_2 = QtWidgets.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(-3, 43, 361, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(224, 84, 121, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(12, 96, 60, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(93, 94, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(223, 160, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_33.setGeometry(QtCore.QRect(93, 20, 113, 21))
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.label_35 = QtWidgets.QLabel(self.tab_4)
        self.label_35.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.label_35.setObjectName("label_35")
        self.line_3 = QtWidgets.QFrame(self.tab_4)
        self.line_3.setGeometry(QtCore.QRect(0, 48, 541, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_34.setGeometry(QtCore.QRect(70, 20, 91, 21))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.label_36 = QtWidgets.QLabel(self.tab_5)
        self.label_36.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.label_36.setObjectName("label_36")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_11.setGeometry(QtCore.QRect(171, 12, 171, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.line_7 = QtWidgets.QFrame(self.tab_5)
        self.line_7.setGeometry(QtCore.QRect(0, 44, 361, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_12.setGeometry(QtCore.QRect(40, 67, 271, 41))
        self.pushButton_12.setObjectName("pushButton_12")
        self.line_8 = QtWidgets.QFrame(self.tab_5)
        self.line_8.setGeometry(QtCore.QRect(0, 102, 361, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_13.setGeometry(QtCore.QRect(40, 123, 271, 41))
        self.pushButton_13.setObjectName("pushButton_13")
        self.line_9 = QtWidgets.QFrame(self.tab_5)
        self.line_9.setGeometry(QtCore.QRect(0, 161, 361, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_14.setGeometry(QtCore.QRect(40, 180, 271, 41))
        self.pushButton_14.setObjectName("pushButton_14")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(33, 340, 60, 16))
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(420, 290, 361, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 360, 751, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "SQL ????????????"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????"))
        self.label_9.setText(_translate("MainWindow", "?????????"))
        self.label_10.setText(_translate("MainWindow", "?????????"))
        self.label_11.setText(_translate("MainWindow", "???????????????"))
        self.pushButton_7.setText(_translate("MainWindow", "????????????"))
        self.label_21.setText(_translate("MainWindow", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "????????????"))
        self.label_7.setText(_translate("MainWindow", "????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "????????????"))
        self.label_8.setText(_translate("MainWindow", "????????????"))
        self.pushButton_6.setText(_translate("MainWindow", "????????????"))
        self.label_22.setText(_translate("MainWindow", "??????????????????"))
        self.label_12.setText(_translate("MainWindow", "????????????"))
        self.label_13.setText(_translate("MainWindow", "????????????"))
        self.pushButton_10.setText(_translate("MainWindow", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "????????????"))
        self.label_4.setText(_translate("MainWindow", "????????????"))
        self.label_34.setText(_translate("MainWindow", "??????????????????"))
        self.pushButton_8.setText(_translate("MainWindow", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_3), _translate("MainWindow", "????????????"))
        self.pushButton_9.setText(_translate("MainWindow", "????????????"))
        self.label_5.setText(_translate("MainWindow", "????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "????????????"))
        self.label_35.setText(_translate("MainWindow", "??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_4), _translate("MainWindow", "????????????"))
        self.label_36.setText(_translate("MainWindow", "????????????"))
        self.pushButton_11.setText(_translate("MainWindow", "???????????????????????????"))
        self.pushButton_12.setText(_translate("MainWindow", "???????????????????????????????????? 1000 ?????????"))
        self.pushButton_13.setText(_translate("MainWindow", "??????????????????????????????????????????"))
        self.pushButton_14.setText(_translate("MainWindow", "???????????????????????? 10 ??????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_5), _translate("MainWindow", "????????????"))
        self.label_6.setText(_translate("MainWindow", "???????????????"))
