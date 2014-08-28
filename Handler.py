#coding:utf-8
__author__ = 'xiejiati'

import view
import model
import translator
import variables
from final_ui.product_value_ui import *
from PySide.QtCore import *
import computer

class ProductionValueHandler(QObject):
    def __init__(self):
        super().__init__()
        self.lastComboxIdx = 0
        self.ui = MainWindow()
        self.ui.pushButton.clicked.connect(self, SLOT('save_slot()'))
        self.ui.pushButton_2.clicked.connect(self, SLOT('compute_export_slot()'))
        self.ui.comboBox.currentIndexChanged[int].connect(self, SLOT('index_changed_slot(int)'))
        self.view = view.ProdutionValueView()
        self.model = model.Model()
        self.translator = translator.Translator()
        self.computer = computer.ProductValue()

    def compute_export_slot(self):
        for name in self.__names__():
            self.computer.product_value()

    def __names__(self):
        path = util.join_path(variables.names_pre_path, \
                              '名字', r'txt')
        lines = self.model.read(path)
        names = []
        for line in lines:
            names.append(line.strip())
        return  names


    def save_slot(self):
        truck_name = self.view.current_truck_name(self.ui)
        self.__save_from_view_2_stored__(truck_name)


    def index_changed_slot(self, index):
        if self.lastComboxIdx != 0:
            last_truck_name = self.view.truck_name(self.lastComboxIdx, self.ui)
            self.__save_from_view_2_stored__(last_truck_name)

        self.ui.tableWidget.setEnabled(index != 0)
        self.lastComboxIdx = index

        current_truck_name = self.view.current_truck_name(self.ui)
        path = util.join_path(variables.path_product_value_package, current_truck_name, r'pv')
        lines = self.model.read(path)
        if lines:
            lines = self.translator.stored_2_view(lines)
            self.view.write(lines, self.ui)
        else:
            self.view.clear_table_text(self.ui)


    def __save_from_view_2_stored__(self, truck_name):
        data = self.view.read(self.ui)
        lines = self.translator.view_2_stored(data)
        path = util.join_path(variables.path_product_value_package, truck_name, r'pv')
        self.model.write(lines, path)

    def ui_show(self):
        return self.ui.show()



class OthersHandler:
    def money_days_off(self):
        pass






#print (translator().stored_2_handler()[1])
#print (product_handler().oil('甲', translator().stored_2_handler()[1]))
#print (product_handler().product_value('甲', translator().stored_2_handler()[1]))
#print (product_handler().miles('已', translator().stored_2_handler()[1]))













