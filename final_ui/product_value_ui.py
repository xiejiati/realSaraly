__author__ = 'xjt'


from complied_ui.production_value import *

class MainWindow(QtGui.QMainWindow, Ui_ProductValue):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.setupUi(self)