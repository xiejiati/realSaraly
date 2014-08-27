#coding:utf-8
__author__ = 'xiejiati'

import view
import model
import translator
import variables
import util
from final_ui.product_value_ui import *
from PySide.QtCore import *

class ProductionValueHandler(QObject):
    def __init__(self):
        super().__init__()
        self.lastComboxIdx = 0
        self.ui = MainWindow()
        self.ui.pushButton.clicked.connect(self, SLOT('save_slot'))
        self.ui.comboBox.currentIndexChanged.connect(self, SLOT('index_changed_slot'))
        self.view = view.ProdutionValueView(self.ui)
        self.model = model.Model()
        self.translator = translator.Translator()

    def save_slot(self):
        truck_name = self.view.current_truck_name()
        self.__save_from_view_2_stored__(truck_name)


    def index_changed_slot(self):
        if self.lastComboxIdx != 0:
            last_truck_name = self.view.truck_name(self.lastComboxIdx)
            self.__save_from_view_2_stored__(last_truck_name)

        self.lastComboxIdx = index

        current_truck_name = self.view.current_truck_name()
        path = util.join_path(variables.path_product_value_package, current_truck_name, r'pv')
        lines = self.model.read(path)
        if lines:
            self.view.write(lines)


    def __save_from_view_2_stored__(self, truck_name):
        data = self.view.read()
        lines = self.translator.view_2_stored(data)
        path = util.join_path(variables.path_product_value_package, truck_name, r'pv')
        self.model.write(lines, path)

    def ui(self):
        return self.ui

class OthersHandler:
    def money_days_off(self):
        pass






#print (translator().stored_2_handler()[1])
#print (product_handler().oil('甲', translator().stored_2_handler()[1]))
#print (product_handler().product_value('甲', translator().stored_2_handler()[1]))
#print (product_handler().miles('已', translator().stored_2_handler()[1]))













