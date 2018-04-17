#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as d
#print(d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"))
# 2017.12.17-09:51:07
def send_email(smtpserver="smtp.mxhichina.com",port='25',sender='gaoxin@begoit.com',password='Gaoxin123',receiver=['gaoxin@begoit.com'],file_path='E:\\framework_jiekou\\report\\result.html'):
    #发送相关的参数
    # smtpserver=""   #发件服务器
    # port=0          #端口
    # sender=""       #账号
    # password=""     #密码
    # receiver=['','']    #多个接收人
    #receiver=''         #单个收件人

    '''编辑邮件的内容'''
    #读文件
#    file_path='result.html'
    with open(file_path,'rb') as fp:
        mail_body=fp.read()


    time=d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    subject=time+'自动化测试报告'
    #body='<p>正文</p>'   #定义邮件正文为html格式
    #msg=MIMEText(body,'html','utf-8')
    msg=MIMEMultipart()
    msg['from']=sender
    msg['to']=';'.join(receiver)  #多个收件人
    # msg['to']=receiver     #单个收件人
    msg['subject']=subject

    #正文
    body=MIMEText(mail_body,"html", "utf-8")
    msg.attach(body)

    #附件
    att=MIMEText(mail_body,'base64','utf-8')
    att['Content-type']='application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)


    #发送邮件
    try:
        '''163/阿里邮箱'''
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver)                        #连接服务器
        smtp.login(sender,password)                     #登录
    except:
        '''QQ邮箱'''
        smtp=smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender,password)
    smtp.sendmail(sender,receiver,msg.as_string())  #发送
    smtp.quit()                                     #关闭

if __name__=='__main__':
    send_email()