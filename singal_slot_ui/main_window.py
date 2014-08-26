__author__ = 'xjt'

from complied_ui.production_value import *
import view



class MainWindow(QtGui.QMainWindow, Ui_ProductValue):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(view.ProdutionValueView.request_save)
        self.pushButton.clicked.connect(view.ProdutionValueView.request_save)


