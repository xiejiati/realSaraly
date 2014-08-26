__author__ = 'xjt'

from PySide.QtCore import *
from PySide.QtGui import *
import sys

app = QApplication(sys.argv)
w = QWidget()
t = QTableWidget(w)
t.setItem(0,1, QLineEdit())
w.show()
sys.exit(app.exec_())
