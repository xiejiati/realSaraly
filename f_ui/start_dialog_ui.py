__author__ = 'xjt'

from c_ui.start_dialog import *

class StartDialog(QtGui.QMainWindow, Ui_StartDialog):
    def __init__(self, parent = None):
        super(StartDialog, self).__init__()
        self.setupUi(self)