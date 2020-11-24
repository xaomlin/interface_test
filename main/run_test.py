#coding:utf-8
from base.run_main import RunMain
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
# from util.operation_excel import operation_excel
class RunTest(object):
	def __init__(self):
		self.run = RunMain()
		self.getdata = GetData()
		self.commonutil = CommonUtil()

	def go_to_run(self):
		p,f,count = 0,0,0
		#获取行数
		test_count = self.getdata.get_case_line()
		# print(test_count)
		for i in range(1,test_count):
			
			is_run = self.getdata.get_is_run(i)
			if is_run:
				# print(i)
				url = self.getdata.get_request_url(i)
				# print(url)
				methon = self.getdata.get_request_way(i)
				# print(methon)
				data = self.getdata.getdata(i)
				cookie = self.getdata.get_cookie(i)
				expect = self.getdata.get_expect_data(i)
				# res = None
				#依赖caseID
				depent_case = self.getdata.is_depend(i)
				# print(depent_case)
				self.depend = DependentData(depent_case)
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
					self.getdata.write_result(i,'pass')
					p = p+1
					# print('测试通过')
				else:
					self.getdata.write_result(i,res)
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