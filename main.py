__author__ = 'xjt'

from PySide.QtCore import *
from PySide.QtGui import *
import sys
from UI.main_window import *
from UI.view import *

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
