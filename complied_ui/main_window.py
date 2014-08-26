__author__ = 'xjt'

from UI.main_ui import *
from PySide import QtCore, QtGui
from UI.view import *


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.__handle_combox_index_changed__)
        self.pushButton.clicked.connect(self.__handle_button_push__)

    def __handle_combox_index_changed__(self, index):
        pass


    def __handle_button_push__(self):
        v = ProdutionView()
        print (v.read(self.tableWidget))




