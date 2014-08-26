__author__ = 'xjt'

from complied_ui.production_value import *
import handler
from PySide.QtGui import *
import sys

class MainWindow(QtGui.QMainWindow, Ui_ProductValue):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.handler = handler.ProductionValueHandler(self)
        self.comboBox.currentIndexChanged[int].connect(index_changed_slot)
        self.pushButton.clicked.connect(save_slot)

def save_slot():
    w.handler.save_slot()

def index_changed_slot(index):
    w.handler.index_changed_slot(index)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()