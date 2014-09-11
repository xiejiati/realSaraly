#coding:utf-8
__author__ = 'xiejiati'

import view
import translator
from final_ui.product_value_ui import *
from final_ui.start_dialog_ui import *
from PySide.QtCore import *
import computer
import model
import variables
import util
from final_ui.other_fee_ui import *
import functools
import os

class ProductionValueHandler(QObject):
    def __init__(self):
        super().__init__()
        self.lastComboxIdx = 0
        self.ui = MainWindow()
        self.other_fee_ui = OtherFeeWindow()
        self.start_dialog = StartDialog()

        self.ui.pushButton.clicked.connect(self, SLOT('save_slot()'))
        self.ui.pushButton_2.clicked.connect(self, SLOT('compute_export_slot()'))
        self.ui.comboBox.currentIndexChanged[int].connect(self, SLOT('index_changed_slot(int)'))
        self.ui.pushButton_3.clicked.connect(self, SLOT('other_fee_open_slot()'))
        self.other_fee_ui.pushButton.clicked.connect(self, SLOT('other_fee_save_slot()'))
        self.start_dialog.pushButton.clicked.connect(self, SLOT('start_accept_slot()'))

        self.view = view.ProdutionValueView()
        self.model = model.CommonFileModel()
        self.translator = translator.ProductValueTranslator()
        self.computer = computer.ProductValueComputer()
        self.xsl_model = model.XslModel()
        self.other_fee_translator = translator.OtherFeeTranslator()
        self.other_fee_view = view.OtherFeeView()
        self.other_fee_computer = computer.OtherFeeComputer()
        self.driver_truck_dict = {}

    def start_accept_slot(self):
        cur_idx_year = self.start_dialog.comboBox.currentIndex()
        year = self.start_dialog.comboBox.itemText(cur_idx_year).strip()
        cur_idx_month = self.start_dialog.comboBox_2.currentIndex()
        month = self.start_dialog.comboBox_2.itemText(cur_idx_month).strip()
        title = "南峰货运" + '  ' + year+'年'+month+'月'
        if int(month) < 10:
            month = '0'+month
        in_year_month = year+month
        variables.pre_path_personal_details_xsl = path_stored+'\\'+in_year_month+pre_path_personal_details_xsl
        variables.pre_path__product_value_stored = path_stored+'\\'+in_year_month+pre_path__product_value_stored
        variables.pre_path_other_fee = variables.pre_path_sum_xsl = path_stored+'\\'+in_year_month
        if not os.path.exists(variables.pre_path__product_value_stored):
            os.makedirs(variables.pre_path__product_value_stored)
        if not os.path.exists(variables.pre_path_personal_details_xsl):
            os.makedirs(variables.pre_path_personal_details_xsl)
        self.start_dialog.close()
        self.ui.setWindowTitle(title)
        self.ui.show()

    def compute_export_slot(self):
        self.save_slot()
        sum_data = self.__personal_detail__()
        self.__salary_list__(sum_data)

    def __salary_list__(self, data):
        xls_data = []
        xls_head_data = []
        xls_head_data.append('序')
        xls_head_data.extend(variables.string_sum_items)
        xls_data.append(xls_head_data)
        i = 0
        total = 0
        for data1 in data:
            i += 1
            items = list(data1.items())
            items.sort(key=functools.cmp_to_key(util.sum_sort_cmp))
            out_data1 = []
            out_data1.append(i)
            out_data1.extend([item[1] for item in items])
            total += out_data1[-1]
            xls_data.append(out_data1)
        row_total = []
        row_total.append(variables.string_total)
        row_total.append(total)
        xls_data.append(row_total)

        path = util.join_path(variables.pre_path_sum_xsl, variables.string_salary_table, 'xls')
        self.xsl_model.single_array_write(path, xls_data, variables.string_salary_table)

        xls_data_salary_sheet = []
        header = xls_data[0][1:]
        j = 1
        num_line = len(xls_data)
        while j < num_line:
            xls_data_salary_sheet.append(header)
            xls_data_salary_sheet.append(xls_data[j][1:])
            xls_data_salary_sheet.append([])
            j += 1

        path = util.join_path(variables.pre_path_sum_xsl, variables.string_salary_sheet, 'xls')
        return self.xsl_model.single_array_write(path, xls_data_salary_sheet, variables.string_salary_sheet)

    def __personal_detail__(self):
        out_data = []
        path_names = util.join_path(variables.names_pre_path, \
                              variables.file_name_drivers, r'txt')
        lines_name = self.model.read(path_names)
        lines_name = util.lines_vaild_data(lines_name)
        for driver_name in lines_name:
            out_data1 = {}
            out_data1[variables.string_sum_driver] = driver_name

            xls_data = []
            driver_name = driver_name.strip()
            truck_name = util.truck_name_by_driver_name(self.driver_truck_dict, driver_name)
            if not truck_name: return

            #truck_name
            out_data1[variables.string_sum_truck] = truck_name
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
                                   self.computer.money_product_value_double(product_value_dict[variables.cooperative])
                                    )
            product_value_total = self.computer.money_product_value(product_value_dict)

            #total product_value:including single and double
            out_data1[variables.string_sum_product_value] = product_value_total
            out_data1[variables.string_sum_tie] = self.computer.money_tie_in_product_value(product_value_total)
            out_data1[variables.string_sum_commission] = self.computer.money_salary_in_product_value(product_value_total)
            util.xls_generate_line(data_product_value_money, variables.string_total,
                                   product_value_total)
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

            #oil saved
            out_data1[variables.string_sum_remaining_oil] = oil_saved

            util.xls_generate_line(data_oil, variables.string_oil_saved, oil_saved)
            util.xls_generate_line(data_oil, variables.string_money_per_oil_liter,
                                   variables.money_per_liter)
            money_oil_saved = self.computer.money_oil_saved(oil_saved)

            #money_oil_saved
            out_data1[variables.string_sum_money_oil] = money_oil_saved
            util.xls_generate_line(data_oil, variables.string_money_oil_saved,
                                   money_oil_saved)
            xls_data.append(data_oil)

            #other fee
            path = util.join_path(variables.pre_path_other_fee, variables.file_name_other_fee,
                              variables.postfix_other_fee)
            lines = self.model.read(path)
            assert (lines)
            other_fee_handler_data = self.other_fee_translator.stored_2_handler(lines)
            other_fee_record = util.other_fee_record_by_name(other_fee_handler_data, driver_name)
            if other_fee_record:
                data_other_fee = []
                util.xls_generate_line(data_other_fee, variables.other_fee_days_off,
                                       float(other_fee_record[variables.other_fee_days_off]))
                util.xls_generate_line(data_other_fee, variables.string_other_fee_deduction_per_day,
                                       variables.money_per_dayoff)
                money_deduction_days_off = self.other_fee_computer.deduction_days_off(float(other_fee_record[variables.other_fee_days_off]))
                util.xls_generate_line(data_other_fee, variables.string_other_fee_days_off_deduction,
                                        money_deduction_days_off)
                util.xls_generate_line(data_other_fee, variables.string_other_fee_actual_phone_fee,
                                       float(other_fee_record[variables.other_fee_phone_fee]))
                phone_fee_deduction = self.other_fee_computer.deduction_phone_fee(float(other_fee_record[variables.other_fee_phone_fee]))
                util.xls_generate_line(data_other_fee, variables.string_other_fee_phone_fee_deduction,
                                       phone_fee_deduction)
                money_phone_fee_ss = self.other_fee_computer.phone_fee_days_off_deduction(phone_fee_deduction, money_deduction_days_off)

                #phone fee and ss
                out_data1[variables.string_sum_tel_ss] = money_phone_fee_ss

                deduction_fee_string = str(other_fee_record[variables.other_fee_deduction])
                deduction_fee_float = 0.0
                if deduction_fee_string == '':
                    deduction_fee_float = float(0)
                else:
                    deduction_fee_float = float(deduction_fee_string)
                out_data1[variables.string_sum_deduction] = deduction_fee_float
                util.xls_generate_line(data_other_fee, variables.string_other_fee_deduction,
                                       deduction_fee_float)

                deduction_total = self.other_fee_computer.deduction_total(money_phone_fee_ss,
                                deduction_fee_float)

                util.xls_generate_line(data_other_fee, variables.string_total, deduction_total)
                out_data1[variables.string_sum_deduction_reason] = other_fee_record[other_fee_comment]
                util.xls_generate_line(data_other_fee, variables.string_other_fee_comment,
                                       other_fee_record[other_fee_comment])

                xls_data.append(data_other_fee)


            out_data1[string_sum_total] = computer.actual_salary(product_value_total,
                                   money_oil_saved,
                                   out_data1[variables.string_sum_tel_ss],
                                   out_data1[variables.string_sum_deduction]
                                   )

            out_data.append(out_data1)

            path = util.join_path(util.pre_path_personal_details_xsl, driver_name, 'xls')
            self.xsl_model.multi_array_write(path, xls_data, variables.string_personal_detail)
        return out_data

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
        path = util.join_path(variables.pre_path__product_value_stored, current_truck_name, r'pv')
        lines = self.model.read(path)
        if lines:
            lines = self.translator.stored_2_view(lines)
            self.view.write(lines, self.ui)
        else:
            self.view.clear_table_text(self.ui)

    def other_fee_open_slot(self):
        self.other_fee_ui.show()
        path = util.join_path(variables.pre_path_other_fee, variables.file_name_other_fee,
                              variables.postfix_other_fee)
        lines = self.model.read(path)
        if not lines: return
        view_data = self.other_fee_translator.stored_2_view(lines)
        self.other_fee_view.write(self.other_fee_ui, view_data)

    
    def other_fee_save_slot(self):
        lines = self.other_fee_view.read(self.other_fee_ui)
        lines = self.other_fee_translator.view_2_stored(lines)
        path = util.join_path(variables.pre_path_other_fee, variables.file_name_other_fee,
                              variables.postfix_other_fee)
        self.model.write(lines, path)

    def __save_from_view_2_stored__(self, truck_name):
        data = self.view.read(self.ui)
        lines = self.translator.view_2_stored(data)
        path = util.join_path(variables.pre_path__product_value_stored, truck_name, r'pv')
        self.model.write(lines, path)

    def ui_show(self):
        return self.start_dialog.show()







#print (translator().stored_2_handler()[1])
#print (product_handler().oil('甲', translator().stored_2_handler()[1]))
#print (product_handler().product_value('甲', translator().stored_2_handler()[1]))
#print (product_handler().miles('已', translator().stored_2_handler()[1]))













