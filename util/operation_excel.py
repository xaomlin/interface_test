#coding:utf-8
import xlrd
from xlutils.copy import copy
from util.opea_case_excel import OperaCaseExcel
from util.common_util import CommonUtil
import os
work_path = os.path.abspath('.')
class OperationExcel(object):
	def __init__(self, file_name=None, sheet_id=0):
		#case_excel返回的case_name、json_name列表
		oce = OperaCaseExcel()
		self.res = oce.get_case_excel_name()
		file_name = self.res[0]
		if file_name:
			self.file_name = os.path.join(work_path,'data_config',file_name)
			self.sheet_id = sheet_id
		else:
			self.file_name = os.path.join(work_path,'data_config/inte.xlsx')
			self.sheet_id = 0
		self.getData = self.get_data()

	#获取sheet内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	#获取单元格行数
	def get_rows(self):
		rows = self.getData.nrows
		return rows

	#获取单元格的内容
	def get_cell_value(self,row,col):
		cell_value = self.getData.cell_value(row,col)
		return cell_value

	#写入数据
	def write_value(self, row, col, value):
		#获取当前时间
		lotime = CommonUtil.get_localtime(self)
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		write_sheet_data = write_data.get_sheet(0)
		write_sheet_data.write(row, col, value)
		# save_file = os.path.join(work_path,'result',lotime,self.res[0])
		# n = self.res[0].split('.')
		# save_name = os.path.join(work_path,'result',lotime,n[0]+'.xls')
		# write_data.save(save_name)
		place = os.path.join(work_path,'/result')
		write_data.save(place + lotime + self.res[0])

	#根据某一列的内容
	def get_col_data(self,col_id=None):
		if col_id:
			cols = self.getData.col_values(col_id)
		else:
			cols = self.getData.col_values(0)
		return cols

	#根据case_id找到对应的行号
	def get_row_num(self,case_id):
		# num = 0
		cols_data = self.get_col_data()
		num = cols_data.index(case_id)
		# print(num)
		return num
		# print(cols_data)
		# for i in cols_data:
		# 	if cols_data[i] == case_id:
		# 		return num
		# 	num = num + 1

	#根据行号找到该行的内容
	def get_row_value(self,row):
		tables = self.getData
		rows_data = tables.row_values(row)
		return rows_data

	#获得行的内容--->上面两个方法结合起来
	def get_row_data(self,case_id):
		row_num = self.get_row_num(case_id)
		row_data = self.get_row_value(row_num)
		return row_data



if __name__ == '__main__':
	op = OperationExcel()
	# print(op.get_data().nrows)
	print(op.get_rows())
	# print(op.get_cell_value(5,3))
	# oe = OperationExcel('../data_config/inter.xlsx',1)
	# print(oe.get_rows())
	# print(oe.get_cell_value(1,1))