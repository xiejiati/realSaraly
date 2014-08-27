__author__ = 'qing'

from PySide import QtCore
from final_ui.product_value_ui import *
QtCore.QObject.connect(MainWindow, QtCore.SIGNAL('clicked()'), QtCore.SLOT('save_slot()'))
QtCore.QObject.connect(MainWindow, QtCore.SIGNAL('clicked()'), QtCore.SLOT('index_changed_slot'))
