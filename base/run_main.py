#coding:utf-8
import requests
import json
class RunMain(object):


	def run_get(self,url,data = None,headers = None):
		res = None
		if headers:
			res = requests.get(url = url,data = data,headers = headers,verify = False)
		else:
			res = requests.get(url = url,data = data,verify = False)
		# print(res.status_code)#查看状态码
		return res.json()

	def run_post(self,url,data = None,headers = None):
		res = None
		if headers:
			res = requests.post(url = url,data = data,headers = headers,verify = False)
		else:
			res = requests.post(url = url,data = data,verify = False)
		# print(res.status_code)#查看状态码
		# print(type(res))
		# print(res.json())
		# return res
		return res.json()

	def run_main(self,method,url,data = None,headers = None):
		res = None
		if method == 'GET':
			res = self.run_get(url,data,headers)
		else:
			res = self.run_post(url,data,headers)
		return json.dumps(res,ensure_ascii = False,sort_keys = True,indent = 2)

if __name__ == '__main__':
	run = RunMain()
	url = 'http://120.78.137.135:8085/comApi/TsetController/testPostBuy'
	data = {
		'userNo':123
	}
	headers = {
		'content-type':'application/json'
	}
	url1 = 'http://120.78.137.135:8085/comApi/TsetController/testPostLogin'
	data1 = {
		'userName' : 'admin',
		'password' : '123456'
	}
	url2 = 'https://www.imooc.com/passport/user/login'
	data2 = {
		'username':'15807686844',
		'password':'lin0921.',
		'verify':'',
		'referer':'https://www.imooc.com'
	}
	res = run.run_post(url2,data2)
	print(res)
	resopesn = res['data']['url'][0]
	request_url = resopesn + '&callback=jQuery191007443657948121962_1586789979831&_=1586789979832'
	res_cookie = requests.get(request_url).cookies
	cookie = requests.utils.dict_from_cookiejar(res_cookie)
	# print(cookie['apsid'])
	url = 'https://order.imooc.com/pay/submitorder?&callback=jQuery191007443657948121962_1586789979831&_=1586789979832'
	res = requests.get(url = url,cookies = cookie,verify = False).text
	print(res)

	# print(run.run_main('POST',url,data,headers))
	# print(run.run_main('POST',url1,data1))