#coding:utf-8
from unittest import mock

#模拟mock封装
def  mock_test(mock_method,url,method,response_data,request_data = None):
	mock_method = mock.Mock(return_value = response_data)
	res = mock_method(url,method,request_data)
	return res