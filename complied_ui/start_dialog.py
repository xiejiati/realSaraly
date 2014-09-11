# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\xjt\Desktop\start_StartDialog.ui'
#
# Created: Wed Sep 10 21:16:19 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import time

class Ui_StartDialog(object):
    def setupUi(self, StartDialog):
        StartDialog.setObjectName("StartDialog")
        StartDialog.resize(300, 100)
        self.widget = QtGui.QWidget(StartDialog)

        self.widget.setGeometry(QtCore.QRect(10, 10, 300, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(300, 50))

        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.comboBox = QtGui.QComboBox(StartDialog)
        self.comboBox.setObjectName("comboBox")
        cur_time = time.localtime(time.time())
        cur_year = int(time.strftime('%Y', cur_time))
        for year in range(cur_year-2, cur_year+11):
            self.comboBox.addItem(str(year))
        self.comboBox.setCurrentIndex(2)
        self.horizontalLayout.addWidget(self.comboBox)

        self.label = QtGui.QLabel(StartDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_2 = QtGui.QComboBox(StartDialog)
        self.comboBox_2.setObjectName("comboBox_2")
        cur_mon = int(time.strftime('%m', cur_time))
        for month in range(1, 13):
            self.comboBox_2.addItem(str(month))
        self.comboBox_2.setCurrentIndex(int(cur_mon)-1)
        self.horizontalLayout.addWidget(self.comboBox_2)

        self.label_2 = QtGui.QLabel(StartDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)


        self.pushButton = QtGui.QPushButton(StartDialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 55, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(StartDialog)

    def retranslateUi(self, StartDialog):
        StartDialog.setWindowTitle(QtGui.QApplication.translate("StartDialog", "请选择日期", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("StartDialog", "年", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("StartDialog", "月", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("StartDialog", "确定", None, QtGui.QApplication.UnicodeUTF8))
