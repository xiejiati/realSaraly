#coding:utf-8
__author__ = 'xjt'

from complied_ui.other_fee import *

class OtherFeeWindow(QtGui.QMainWindow, Ui_OtherFeeWindow):
    def __init__(self, parent = None):
        super(OtherFeeWindow, self).__init__()
        self.setupUi(self)