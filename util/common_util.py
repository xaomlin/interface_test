#coding:utf-8
import sys
import time

class CommonUtil(object):
	def is_contain(self,str_one,str_two):
		'''
		str_one:预期结果
		str_two:实际结果
		'''
		flag = None
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag
	#获取当前时间
	def get_localtime(self):
		# res = time.strftime('%Y%m%d%H%M%S',time.localtime())
		res = time.strftime('%Y%m%d',time.localtime())
		return res
if __name__ == '__main__':
	c = CommonUtil()
	print(c.get_localtime())