import json
import requests

class RunMain:
	# def __init__(self,method,url,data = None):
	# 	self.res = self.run_main(method,url,data)

	def send_post(self,url ,data,headers = None):
		res = requests.post(url = url,data = data,headers=None,)
		return res.json()
		# return json.dumps(res,indent =2,sort_keys = True)
	# print(send_post(url ,data))
	def send_get(self,url ,data):
		res = requests.get(url = url,data = data).json()
		return res
		# return json.dumps(res,indent =2,sort_keys = True)
	# print(send_post(url ,data))

	def run_main(self,method,url,data = None):
		res = None
		if method == 'GET':
			res = self.send_get(url,data)
		if method == 'POST':
			res = self.send_post(url,data)
		return res


if __name__ == '__main__':
	url = 'http://120.78.137.135:8085//comApi/TsetController/testDataGet?params=1'
	url1 = 'https://www.imooc.com/passport/user/login'
	data1 = {
		'username':'15807686844',
		'password':'M2J42iBD3bXkPYEC9UFYRJkX5Z5t8cqEWxwMRb08PMidEuZ+SDK8oiRPKAtWATHBaTZfV0vxzW1gKaQHmrY2d/hdwfdZfA3Xd4y4CfK9VqtCOk4uqvtjk3qyUZe2B4RW2D/Gn+mQb8a3S9Ns79vGz0GSBZtf+Hy70OCu+8Ri0Rc=',
		'verify':'',
		'remember':'1',
		'pwencode':'1',
		'browser_key':'8ab1b855e36715051c90c54c59778c97'
	}
	run = RunMain()
	res = run.run_main('POST',url1,data1)
	print(res)

	# print(run.run_main('GET',url))
	# print(run.run_main('POST',url1,data1))