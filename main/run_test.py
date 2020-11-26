#coding:utf-8
from base.run_main import RunMain
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.opea_case_excel import OperaCaseExcel
from util.logger import Logger

class RunTest(object):
	def __init__(self):
		self.run = RunMain()
		self.commonutil = CommonUtil()
		self.operacaseexcel = OperaCaseExcel()

	def go_to_run(self):
		operacaseexcel = OperaCaseExcel()
		'''获取需执行的xlsx及json文件,返回的是res列表,里面嵌套元组(xlsx名，json文件名)'''
		run_data = operacaseexcel.get_case_name()
		rang = len(run_data)
		'''循环run_data列表，分别获取xlsx名字与json文件名'''
		for i in range(0, rang):
			xlsx_data = run_data[i][0]
			json_data = run_data[i][1]
			logger = Logger(logger=xlsx_data).getlog()
			logger.info('测试开始')
			logger.info('获取json文件：%s', json_data)

			p,f,count = 0,0,0

			getdata = GetData(xlsx_data)
			#获取行数
			test_count = getdata.get_case_line()

			for i in range(1,test_count):
				is_run = getdata.get_is_run(i)
				if is_run:
					# print(i)
					url = getdata.get_request_url(i)
					# print(url)
					methon = getdata.get_request_way(i)
					# print(methon)
					data = getdata.getdata(i,json_data)
					cookie = getdata.get_cookie(i)
					expect = getdata.get_expect_data(i)
					#依赖caseID
					depent_case = getdata.is_depend(i)
					# print(depent_case)
					#self.depend = DependentData(depent_case)
					#method,url,data = None,cookie = None
					if depent_case != None:

						print(self.depend.get_case_id_data())
						#依赖响应数据
						depend_response_data = self.depend.get_key_for_data(i)
						print(depend_response_data)
						#获取依赖的key
						depend_key = self.getdata.get_dependent_data(i)
						# print(depend_key)
						data[depend_key] = depend_response_data
						# print(data)
					# print(methon,url,data)
					res = self.run.run_main(methon,url,data,cookie)
					# print(res)
					if self.commonutil.is_contain(expect,res):
						getdata.write_result(i,'pass')
						p = p+1
						# print('测试通过')
					else:
						getdata.write_result(i,res)
						f = f+1
						# print(res)
			count = p+f
			print(p)
			print(f)
			print(count)
			return res
			


if __name__ == '__main__':
	r = RunTest()
	r.go_to_run()