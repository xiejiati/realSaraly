#coding:utf-8
__author__ = 'xiejiati'

import view
import translator
from final_ui.product_value_ui import *
from PySide.QtCore import *
import computer
import model
import variables
import util

class ProductionValueHandler(QObject):
    def __init__(self):
        super().__init__()
        self.lastComboxIdx = 0
        self.ui = MainWindow()
        self.ui.pushButton.clicked.connect(self, SLOT('save_slot()'))
        self.ui.pushButton_2.clicked.connect(self, SLOT('compute_export_slot()'))
        self.ui.comboBox.currentIndexChanged[int].connect(self, SLOT('index_changed_slot(int)'))
        self.view = view.ProdutionValueView()
        self.model = model.CommonFileModel()
        self.translator = translator.ProductValueTranslator()
        self.computer = computer.ProductValueComputer()
        self.xsl_model = model.XslModel()
        self.driver_truck_dict = {}

    def compute_export_slot(self):
        self.save_slot()
        xls_data = []

        truck_name = util.truck_name_by_driver_name(self.driver_truck_dict, '甲')
        lines = util.combine_path_read(self.model, variables.pre_path__product_value_stored, truck_name, 'pv')

        #orginal product value
        data_org_product_value = self.translator.stored_2_xls(lines)
        xls_data.append(data_org_product_value)

        #total of product value
        total_computer_input = self.translator.stored_2_handler(lines)
        product_value_dict = {}
        product_value_dict = self.computer.product_value('甲', total_computer_input)
        data_product_value_money = []
        util.xls_generate_line(data_product_value_money, '', variables.personal,
                               variables.cooperative)
        util.xls_generate_line(data_product_value_money, variables.string_product_value,
                               product_value_dict[variables.personal],
                               product_value_dict[variables.cooperative])
        util.xls_generate_line(data_product_value_money, variables.string_coe,
                               str(variables.single_commission),
                               str(variables.double_commission))
        util.xls_generate_line(data_product_value_money, variables.string_value,
            str(self.computer.money_product_value_single(product_value_dict[variables.personal])),
            str(self.computer.money_product_value_double(product_value_dict[variables.cooperative])))
        util.xls_generate_line(data_product_value_money, variables.string_total, '',
            str(self.computer.money_product_value(product_value_dict)))
        xls_data.append(data_product_value_money)

        data_miles = []
        util.xls_generate_line(data_miles, '', variables.light_truck,
                               variables.first_level_heavy_truck,
                               variables.second_level_heavy_truck,
                               variables.third_level_heavy_truck)
        miles_dict = self.computer.miles('甲', total_computer_input)
        util.xls_generate_line(data_miles, variables.string_miles,
                               miles_dict[variables.personal][variables.light_truck],
                               miles_dict[variables.personal][variables.first_level_heavy_truck],
                               miles_dict[variables.personal][variables.second_level_heavy_truck],
                               miles_dict[variables.personal][variables.third_level_heavy_truck])
        util.xls_generate_line(data_miles, variables.string_miles,
                               miles_dict[variables.cooperative][variables.light_truck],
                               miles_dict[variables.cooperative][variables.first_level_heavy_truck],
                               miles_dict[variables.cooperative][variables.second_level_heavy_truck],
                               miles_dict[variables.cooperative][variables.third_level_heavy_truck])
        util.xls_generate_line(data_miles, variables.string_total,
        miles_dict[variables.personal][variables.light_truck]+ miles_dict[variables.cooperative][variables.light_truck],
        miles_dict[variables.personal][variables.first_level_heavy_truck]+ miles_dict[variables.cooperative][variables.first_level_heavy_truck],
        miles_dict[variables.personal][variables.second_level_heavy_truck]+ miles_dict[variables.cooperative][variables.second_level_heavy_truck],
        miles_dict[variables.personal][variables.third_level_heavy_truck]+ miles_dict[variables.cooperative][variables.third_level_heavy_truck],
        )
        util.xls_generate_line(data_miles, variables.string_coe,
                               variables.oil_per_mile_by_weight_coe[variables.light_truck],
                               variables.oil_per_mile_by_weight_coe[variables.first_level_heavy_truck],
                               variables.oil_per_mile_by_weight_coe[variables.second_level_heavy_truck],
                               variables.oil_per_mile_by_weight_coe[variables.third_level_heavy_truck]
                               )

        xls_data.append(data_miles)




        
        









        path = util.join_path(util.pre_path_xsl, '甲', 'xls')
        self.xsl_model.org_product_value_write(path, xls_data)




    def __print_product_value_money__(self, driver_name, truck_name, lines):
        data = self.translator.stored_2_handler(lines)
        self.computer._product_value(driver_name, data)

    def __names__(self):
        path = util.join_path(variables.names_pre_path, \
                              variables.file_name_drivers, r'txt')
        lines = self.model.read(path)
        return util.lines_vaild_data(lines)


    def save_slot(self):
        if self.view.truck_combox_index(self.ui) == 0:
            return

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













