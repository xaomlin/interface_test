#coding:utf-8
import sys
import json
from util.operation_excel import OperationExcel
from base.run_main import RunMain
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
from util.opea_case_excel import OperaCaseExcel

class DependentData(object):
	def __init__(self,case_id):
		self.case_id = case_id
		self.data = GetData()
		self.opera_excel = OperationExcel()
	#通过case_id获取case_id的整行数据
	def get_case_id_data(self):
		rows_data = self.opera_excel.get_row_data(self.case_id)
		# print(rows_data)
		return rows_data
	#执行依赖case，获取依赖返回数据
	def run_dependent_case(self):
		#获取行号
		row = self.opera_excel.get_row_num(self.case_id)
		dependent_url = self.data.get_request_url(row)
		# print(dependent_url)
		dependent_data = self.data.getdata(row)
		# print(dependent_data)
		dependent_methon = self.data.get_request_way(row)
		# print(dependent_methon)
		dependent_cookie = self.data.get_cookie(row)
		# res = RunMain().run_post(dependent_url,dependent_data)
		# method,url,data = None,cookie = None
		run_dependent = RunMain()
		res = run_dependent.run_main(dependent_methon,dependent_url,dependent_data,dependent_cookie)
		print(res)
		return res

	#根据依赖的key获取执行依赖测试case，后返回key对应的值
	def get_key_for_data(self,row):
		#获取key
		# data = GetData()
		key = self.data.get_dependent_key(row)
		response_data = self.run_dependent_case()
		res_data = json.loads(response_data)
		print(res_data)
		json_exe = parse(key)
		# print(json_exe)
		# madle = json_exe.find(response_data)
		# return [match.value for math in madle][0]
		return [match.value for match in json_exe.find(res_data)][0]
	def test1(self):
		jsonpath_expr = parse('ortherData.[0].userNo')
		data = {  "code": 200,  "count": 0,  "data": "",  "errorData": "",  "isPage": 0,
  		"limit": 0,  "msg": "登录成功,已返回用户编号",  "operationType": "",  "ortherData": [{
    	"userNo": "U-4515151109911622E7"  }],  "ortherMsg": "",  "page": 0,
      	"totlePage": 0}
      	# data1 = json.loads(data)
		print([match.value for match in jsonpath_expr.find(data)][0])

if __name__ == '__main__':
	test = DependentData('case_13')
	# test.run_dependent_case()
	test.test1()