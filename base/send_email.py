import smtplib
from email.mime.text import MIMEText

class SendEmail(object):
	def send(self,count,pass_count,fail_count):# 第三方 SMTP 服务
		mail_host = "smtp.qq.com"# SMTP服务器
		mail_user = "838303806@qq.com"  # 用户名
		mail_pass = "owipgudxlbtnbegi"  # 密码(这里的密码不是登录邮箱密码，而是授权码)
		sender = '838303806@qq.com'  # 发件人邮箱
		receivers = ['15807686844@163.com']  # 接收人邮箱
		content = '这是一份接口自动化邮件，总共测试%d个接口,通过了%d个，失败了%d个'%(count,pass_count,fail_count)
		title = '接口自动化测试邮件'  # 邮件主题
		message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
		message['From'] = "{}".format(sender)
		message['To'] = ",".join(receivers)
		message['Subject'] = title
		try:
			smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
			smtpObj.login(mail_user, mail_pass)  # 登录验证
			smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
			smtpObj.close()
			print("mail has been send successfully.")
		except smtplib.SMTPException as e:
			print(e)

if __name__ == '__main__':
	send_email = SendEmail()
	send_email.send(10,5,5)