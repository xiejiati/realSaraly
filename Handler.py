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
        path_names = util.join_path(variables.names_pre_path, \
                              variables.file_name_drivers, r'txt')
        lines_name = self.model.read(path_names)
        lines_name = util.lines_vaild_data(lines_name)
        for driver_name in lines_name:
            xls_data = []
            driver_name = driver_name.strip()
            truck_name = util.truck_name_by_driver_name(self.driver_truck_dict, driver_name)
            if not truck_name: return
            lines = util.combine_path_read(self.model, variables.pre_path__product_value_stored, truck_name, 'pv')

            #orginal product value
            data_org_product_value = self.translator.stored_2_xls(lines)
            xls_data.append(data_org_product_value)

            #total of product value
            total_computer_input = self.translator.stored_2_handler(lines)
            product_value_dict = {}
            product_value_dict = self.computer.product_value(driver_name, total_computer_input)
            data_product_value_money = []
            util.xls_generate_line(data_product_value_money, '', variables.personal,
                                   variables.cooperative)
            util.xls_generate_line(data_product_value_money, variables.string_product_value,
                                   product_value_dict[variables.personal],
                                   product_value_dict[variables.cooperative])
            util.xls_generate_line(data_product_value_money, variables.string_coe,
                                   variables.single_commission, variables.double_commission)
            util.xls_generate_line(data_product_value_money, variables.string_value,
                                   self.computer.money_product_value_single(product_value_dict[variables.personal]),
                                   self.computer.money_product_value_double(product_value_dict[variables.cooperative]))
            util.xls_generate_line(data_product_value_money, variables.string_total,
                                   self.computer.money_product_value(product_value_dict))
            xls_data.append(data_product_value_money)

            data_miles = []
            util.xls_generate_line(data_miles, '', variables.light_truck,
                                   variables.first_level_heavy_truck,
                                   variables.second_level_heavy_truck,
                                   variables.third_level_heavy_truck)
            miles_dict = self.computer.miles(driver_name, total_computer_input)
            util.xls_generate_line(data_miles, variables.string_miles_single,
                                   miles_dict[variables.personal][variables.light_truck],
                                   miles_dict[variables.personal][variables.first_level_heavy_truck],
                                   miles_dict[variables.personal][variables.second_level_heavy_truck],
                                   miles_dict[variables.personal][variables.third_level_heavy_truck])
            util.xls_generate_line(data_miles, variables.string_miles_double,
                                   miles_dict[variables.cooperative][variables.light_truck],
                                   miles_dict[variables.cooperative][variables.first_level_heavy_truck],
                                   miles_dict[variables.cooperative][variables.second_level_heavy_truck],
                                   miles_dict[variables.cooperative][variables.third_level_heavy_truck])

            miles_light = self.computer.miles_level_total(miles_dict, variables.light_truck)
            miles_first_level = self.computer.miles_level_total(miles_dict, variables.first_level_heavy_truck)
            miles_second_level = self.computer.miles_level_total(miles_dict, variables.second_level_heavy_truck)
            miles_third_level = self.computer.miles_level_total(miles_dict, variables.third_level_heavy_truck)
            util.xls_generate_line(data_miles, variables.string_total,
                                   miles_light,
                                   miles_first_level,
                                   miles_second_level,
                                   miles_third_level
            )
            util.xls_generate_line(data_miles, variables.string_oil_subsidy_per_mile,
                                   variables.oil_per_mile_by_weight_coe[variables.light_truck],
                                   variables.oil_per_mile_by_weight_coe[variables.first_level_heavy_truck],
                                   variables.oil_per_mile_by_weight_coe[variables.second_level_heavy_truck],
                                   variables.oil_per_mile_by_weight_coe[variables.third_level_heavy_truck]
            )

            util.xls_generate_line(data_miles, variables.string_oil_subsidy,
                                   self.computer.oil_n_miles(miles_light, variables.oil_per_mile_by_weight_coe[variables.light_truck]),
                                   self.computer.oil_n_miles(miles_first_level, variables.oil_per_mile_by_weight_coe[variables.first_level_heavy_truck]),
                                   self.computer.oil_n_miles(miles_second_level, variables.oil_per_mile_by_weight_coe[variables.second_level_heavy_truck]),
                                   self.computer.oil_n_miles(miles_third_level, variables.oil_per_mile_by_weight_coe[variables.third_level_heavy_truck])
            )

            oil_subsidy = self.computer.oil_subsidy_total(miles_dict)
            util.xls_generate_line(data_miles, variables.string_total, oil_subsidy)
            xls_data.append(data_miles)

            data_oil = []
            oil_dict = self.computer.oil(driver_name, total_computer_input)
            util.xls_generate_line(data_oil, variables.string_oil_own_single,
                                   oil_dict[variables.personal])
            util.xls_generate_line(data_oil, variables.string_oil_own_double,
                                   oil_dict[variables.cooperative])
            oil_own = self.computer.oil_total_own(oil_dict)
            util.xls_generate_line(data_oil, variables.string_total, oil_own)
            oil_saved = self.computer.oil_saved(oil_own, oil_subsidy)
            util.xls_generate_line(data_oil, variables.string_oil_saved, oil_saved)
            util.xls_generate_line(data_oil, variables.string_money_per_oil_liter,
                                   variables.money_per_liter)
            util.xls_generate_line(data_oil, variables.string_money_oil_saved,
                                   self.computer.money_oil_saved(oil_saved))
            xls_data.append(data_oil)

            path = util.join_path(util.pre_path_xsl, driver_name, 'xls')
            self.xsl_model.personal_detail_write(path, xls_data)


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













