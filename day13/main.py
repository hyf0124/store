
import os
from HTMLTestRunner import HTMLTestRunner
import  unittest

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")



runner  = HTMLTestRunner.HTMLTestRunner(
    title = "银行测试报告",
    description="开户、存钱、查询、取款、转账报告",
    verbosity=1,
    stream=open(file="ICBC.html",mode="w+",encoding="utf-8")
)

runner.run(tests)

if __name__ == '__main__':
    fromaddr = '2421045399@qq.com'
    password = 'covuvbqsfzfzdjgc'
    toaddrs = ['13552648187@163.com']

    pdfFile = 'ICBC.html'
    pdfApart = MIMEApplication(open(pdfFile,'rb').read())
    pdfApart.add_header('Content-Disposition','attachment',filename = pdfFile)


    m = MIMEMultipart()
    m.attach(pdfApart)
    m['Subject'] = 'ICBC报告'

    try:
        sever = smtplib.SMTP('smtp.qq.com')
        sever.login(fromaddr,password)
        sever.sendmail(fromaddr,toaddrs,m.as_string())
        print('success')
        sever.quit()
    except smtplib.SMTPException as e:
        print('error',e)

