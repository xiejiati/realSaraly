__author__ = 'xjt'

from PySide.QtGui import *
import sys
import handler
app = QApplication(sys.argv)
h = handler.ProductionValueHandler()
h.ui().show()
app.exec_()