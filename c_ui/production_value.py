# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'production_value.ui'
#
# Created: Tue Aug 26 14:08:56 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import util
import variables

class Ui_ProductValue(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 931, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(60)
        self.tableWidget.setEnabled(False)
        self.tableWidget.verticalHeader().setVisible(False)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = QtGui.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsUserCheckable)
                self.tableWidget.setItem(i, j, item)
                if not util.if_need_not_record(i, j):
                    self.tableWidget.item(i, j).setFlags(QtCore.Qt.ItemIsUserCheckable\
                                                         |QtCore.Qt.ItemIsEditable\
                                                        |QtCore.Qt.ItemIsEnabled)
                else:
                    self.tableWidget.item(i, j).setBackground(QtGui.QColor(96,96,96))

        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.comboBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox.setEditable(True)
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setObjectName("comboBox")

        self.trucks = util.get_truck_names()
        for i in range(len(self.trucks)+1):
            self.comboBox.addItem("")

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", variables.date, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", variables.client, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", variables.product_value, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", variables.comment, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", variables.truck_weight, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", variables.oil, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", variables.miles, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindow", variables.drivers, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("MainWindow", variables.from_to, None, QtGui.QApplication.UnicodeUTF8))

        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "请选择车辆", None, QtGui.QApplication.UnicodeUTF8))
        for i in range(len(self.trucks)):
            self.comboBox.setItemText(i+1, QtGui.QApplication.translate("MainWindow", self.trucks[i], None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "保存", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "计算并导出", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "输入话费", None, QtGui.QApplication.UnicodeUTF8))


