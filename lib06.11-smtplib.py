'''
smtplib模块

smtplib模块是smtp简单邮件传输协议客户端的实现，为了通用性，有时候发送邮件的时候要带附件或图片，用email.mime来装载内容。

用Python的 smtplib 发送邮件只需要三步：
1、connect（连接到邮件服务器）
2、login（登陆验证）
3、sendmail（发送邮件）

简单方便。
'''
import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
#msg['from'] = 'hellojue@foxmail.com'
#msg['to'] = 'weiyq10580@hundsun.com'
msg['subject'] = 'test'
content = '''
	你好：
		这是一封自动发送的邮件。
	hellojue@foxmail.com
'''

txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com', '25')
smtp.login('hellojue@foxmail.com','')
smtp.sendmail('hellojue@foxmail.com','weiyq10580@hundsun.com', str(msg))
smtp.quit()