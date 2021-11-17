import smtplib
from email.mime.text import MIMEText
from email.header import Header
import unittest
import time
import os

def send_mail(file_new):


    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login(2551977641@qq.com,)
    smtp.sendmail(****@**.com, ****@**.com, msg.as_string())
    smtp.quit()
    print('email has send out !')
    # 查找测试报告目录，找到最新生成的测试报告文件


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_now
