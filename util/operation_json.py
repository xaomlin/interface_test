#coding:utf-8
# import sys
from util.opea_case_excel import OperaCaseExcel
import json
import os
work_path = os.path.abspath('.')

class OperationJson(object):
	def __init__(self,json_files = None):
		#获取json文件名
		if json_files:
			self.json_files = os.path.join(work_path,'data_config/json文件',json_files)
		else:
			self.json_files = os.path.join(work_path,'data_config/interface.json')
		self.get_json_data = self.get_json()

	#获取json文件
	def get_json(self):
		with open(self.json_files,encoding = "utf-8") as json_file:
			json_data = json.load(json_file)
		return json_data

	#获取json数据
	def get_data(self,json_id = None):
		if json_id:
			return self.get_json_data[json_id]
		else:
			return None


if __name__ == '__main__':
	oj = OperationJson('login.json')
	# print(oj.get_json()['post'])
	print(oj.get_data('login'))
# json_file = open('../data_config/interface.json')
# json_data = json.load(json_file)
# print(json_data['post'])