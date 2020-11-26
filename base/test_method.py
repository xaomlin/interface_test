#coding:utf-8
import unittest
import json
import base.HTMLTestRunner
from unittest import mock
from base.demoClass import RunMain
from base.mock_demo import mock_test

class TestMethod(unittest.TestCase):

	# @classmethod
	# def setUpClas(self):
	# 	sef.run = RunMain()
	def setUp(self):
		self.run = RunMain()

	# @unittest.skip('test01')
	def test01(self):
		# globals()['abc'] = '100'#全局变量
		url = 'http://120.78.137.135:8085//comApi/TsetController/testDataGet?params=2'
		data = {
			"code":100,
			"msg":"请求成功",
			"ortherMsg":"",
			"isPage":0,
			"data":["test1","test2","test3","test4","test5","test6","test7"],
			"ortherData":"",
			"count":"",
			"page":0,
			"limit":0,
			"totlePage":0,
			"errorData":"",
			"operationType":""
		}
		#mock模拟返回数据
		# mock_data = mock.Mock(return_value = data)
		# self.run.run_mainn = mock_data
		# print(mock_data)
		# res = url,methoself.run.run_main('GET',url)
		res = mock_test(self.run.run_main,url,'GET',data)
		self.assertEqual(res['code'],200,'测试失败')
		print(res)
		# print(type(res))

	def test02(self):
		# print(abc)
		url = 'http://120.78.137.135:8085/comApi/TsetController/testDataPost'
		data = {
			'paramsPost':'1'
		}	
		res = self.run.run_main('POST',url,data)
		self.assertEqual(res['code'],200,'测试失败')
		print(res)
		# print(type(res))

if __name__ == '__main__':
	filepath = "../report/htmlreport.html"
	#资源流
	fp = open(filepath,'wb')

	suite = unittest.TestSuite()
	suite.addTest(TestMethod('test01'))
	suite.addTest(TestMethod('test02'))
	unittest.TextTestRunner().run(suite)
	#html报告
	# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = '第一份测试报告')
	# runner.run(suite,rerun=False,save_last_run = True)
