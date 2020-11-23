#coding:utf-8
from util.operation_excel import OperationExcel
from data.dataconfig import dataconfig
from util.operation_json import OperationJson

class GetData(object):
	
	def __init__(self):
		self.opera_excel = OperationExcel()

	#获取行数
	def get_case_line(self):
		return self.opera_excel.get_rows()

	#判断是否执行
	def get_is_run(self,row):
		flag = None
		col = dataconfig.get_isrun()
		is_run = self.opera_excel.get_cell_value(row,col)
		if is_run == 'yes':
			flag =  True
		else:
			flag =  False
		return flag
		
	#判断是否携带cookie
	def get_cookie(self,row):
		flag = None
		col = dataconfig.get_cookie()
		cookie = self.opera_excel.get_cell_value(row,col)
		if cookie == 'yes':
			return dataconfig.get_cookie()
		else:
			return None

	#判断是否有case依赖
	def is_depend(self,row):
		col = dataconfig.get_depend_case()
		depend = self.opera_excel.get_cell_value(row,col)
		if depend == '' :
			return None
		else:
			return depend

	#获取请求方式
	def get_request_way(self,row):
		col = dataconfig.get_request_way()
		request_way = self.opera_excel.get_cell_value(row,col)
		return request_way

	#获取url
	def get_request_url(self,row):
		col = dataconfig.get_url()
		url = self.opera_excel.get_cell_value(row,col)
		return url

	#获取请求数据
	def get_request_data(self,row):
		col = dataconfig.get_data()
		data = self.opera_excel.get_cell_value(row,col)
		if data == '':
			return None
		return data

	#通过请求数据关键字从json获取请求数据
	def getdata(self,row):
		opera_json = OperationJson()
		request_key = self.get_request_data(row)
		request_data = opera_json.get_data(request_key)
		if request_data == '' :
			return None
		else:
			return request_data

	#获取依赖数据的key
	def get_dependent_key(self,row):
		col = dataconfig.get_depend_key()
		depend_key = self.opera_excel.get_cell_value(row,col)
		if depend_key == '':
			return None
		else :
			return depend_key

	#获取数据依赖字段
	def get_dependent_data(self,row):
		col = dataconfig.get_depend_file()
		get_dependent_data = self.opera_excel.get_cell_value(row,col)
		if get_dependent_data == '':
			return None
		else :
			return get_dependent_data

	#获取预期结果
	def get_expect_data(self,row):
		col = dataconfig.get_expect()
		expect_data = self.opera_excel.get_cell_value(row,col)
		if expect_data == '':
			return None
		return expect_data

	#获取写入实际结果行
	def write_result(self,row,value):
		col = dataconfig.get_result()
		write = self.opera_excel.write_value(row,col,value)
		if write == '':
			return None
		return write

	