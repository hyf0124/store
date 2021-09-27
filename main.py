from HTMLTestRunner import HTMLTestRunner
import  unittest

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

tests = unittest.defaultTestLoader.discover(r"D:\pythonProject\day12",pattern = 'Test*.py')
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是计算器测试报告",
    description= "计算器的加法测试报告",
    verbosity=1,
    stream=open(file="计算器报告.html",mode="w+",encoding="utf-8")
)

runner.run(tests)



if __name__ == '__main__':
    fromaddr = '2421045399@qq.com'
    password = 'covuvbqsfzfzdjgc'
    toaddrs = ['13552648187@163.com']

    pdfFile = '计算器报告.html'
    pdfApart = MIMEApplication(open(pdfFile,'rb').read())
    pdfApart.add_header('Content-Disposition','attachment',filename = pdfFile)


    m = MIMEMultipart()
    m.attach(pdfApart)
    m['Subject'] = '计算器报告'

    try:
        sever = smtplib.SMTP('smtp.qq.com')
        sever.login(fromaddr,password)
        sever.sendmail(fromaddr,toaddrs,m.as_string())
        print('success')
        sever.quit()
    except smtplib.SMTPException as e:
        print('error',e)











#多线程
'''
from threading  import Thread



class testadd(Thread):
    name = 'TestCalc1.py'
    while True:
        tests = unittest.defaultTestLoader.discover(r"D:\pythonProject\day12",pattern = name)
        runner = HTMLTestRunner.HTMLTestRunner(
            title = "这是计算器测试报告",
            description= "计算器的加法测试报告",
            verbosity=1,
            stream=open(file="计算器报告加法.html",mode="w+",encoding="utf-8")
        )

        runner.run(tests)
        break


class testminus(Thread):
    name = 'TestCalc2.py'
    while True:
        tests = unittest.defaultTestLoader.discover(r"D:\pythonProject\day12", pattern = name)

        runner = HTMLTestRunner.HTMLTestRunner(
            title="这是计算器测试报告",
            description="计算器的减法测试报告",
            verbosity=1,
            stream=open(file="计算器报告减法.html", mode="w+", encoding="utf-8")
        )

        runner.run(tests)
        break


class testmulti(Thread):
    name = 'TestCalc3.py'
    while True:
        tests = unittest.defaultTestLoader.discover(r"D:\pythonProject\day12", pattern=name)

        runner = HTMLTestRunner.HTMLTestRunner(
            title="这是计算器测试报告",
            description="计算器的乘法测试报告",
            verbosity=1,
            stream=open(file="计算器报告乘法.html", mode="w+", encoding="utf-8")
        )

        runner.run(tests)
        break


class testdevision(Thread):
   name = 'TestCalc4.py'
   while True:
        tests = unittest.defaultTestLoader.discover(r"D:\pythonProject\day12",pattern = name)


        runner = HTMLTestRunner.HTMLTestRunner(
            title = "这是计算器测试报告",
            description= "计算器的除法测试报告",
            verbosity=1,
            stream=open(file="计算器报告除法.html",mode="w+",encoding="utf-8")
        )

        runner.run(tests)
        break


a = testadd()

b = testmulti()

c = testmulti()

d = testdevision()


a.start()
b.start()
c.start()
d.start()
'''
