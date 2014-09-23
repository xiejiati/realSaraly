# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'other_fees.ui'
#
# Created: Tue Sep  2 17:18:04 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from variables import *

class Ui_OtherFeeWindow(object):
    def setupUi(self, OtherFeeWindow):
        OtherFeeWindow.setObjectName("OtherFeeWindow")
        OtherFeeWindow.resize(560, 600)
        self.central_widget = QtGui.QWidget(OtherFeeWindow)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtGui.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtGui.QTableWidget(self.central_widget)
        self.tableWidget.setRowCount(40)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
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
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = QtGui.QTableWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEditable\
                    |QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)

        self.pushButton = QtGui.QPushButton(self.central_widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(698, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        OtherFeeWindow.setCentralWidget(self.central_widget)
        self.statusbar = QtGui.QStatusBar(OtherFeeWindow)
        self.statusbar.setObjectName("statusbar")
        OtherFeeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherFeeWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherFeeWindow)

    def retranslateUi(self, OtherFeeWindow):
        OtherFeeWindow.setWindowTitle(QtGui.QApplication.translate("OtherFeeWindow", "杂项", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("OtherFeeWindow", other_fee_name, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("OtherFeeWindow", other_fee_phone_fee, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("OtherFeeWindow", other_fee_days_off, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("OtherFeeWindow", other_fee_deduction, None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("OtherFeeWindow", other_fee_comment, None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("OtherFeeWindow", "保存", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

