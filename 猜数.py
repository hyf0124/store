'''
import random
i=100#变量i 代表资金
print('初始资金为100，猜一次扣除10,猜0~100之间')
a=input('请输入一个数字')
a=int(a)#变量a定义整形
num=random.randint(0,100)#随机数范围0~100
while a!=num:#条件 a不等于随机数
    i=i-10# i 每次减10
    if i==0:# 条件i 等于0
        print('资金不足')
        break#退出循环
    else :
        if a<num:#条件 a 小于随机数
            print('太小',a)
            a = input('请输入一个数字')#这一步可以重新输入数字
            a = int(a)
        else :#只剩下比随机数大的数了，条件可以不写
            print('太大',a)
            a = input('请输入一个数字')
            a = int(a)
if a==num:#a 等于随机数
    print('猜对了',a)
    print('资金还剩',i)#变量i 随着猜的次数减10 用来表示剩余的资金
'''
'''求和
a=input('请输入一个数字')
a=int(a)
i=0
num=0
while i<9:
    i=i+1
    num=num+a
    a = input('请输入一个数字')
    a = int(a)
print('结果为',num)
'''
'''最大数 平均数
a=input('请输入一个数')
a=int(a)
i=0
num=0
max=0
while i<9:
    i=i+1
    num=num+a
    a = input('请输入一个数')
    a = int(a)
    j=num/10
    if a>max:
         max=a
    else :
        max=max
print('平均数为', j)
print('最大的数为',max)
print('结果为',num)
'''


'''50~100随机数
import random
num=random.randint(50,150)
print(num)
'''
'''判断三角形
a=input('输入一条边的值')
a=int(a)
b=input('再次输入一条边的值')
b=int(b)
c=input('再次输入一条边的值')
c=int(c)
while a+b>c:
    if a==b!=c:
        print('是等腰三角形')
        break
    else :
        if a==b==c:
            print('是等边三角形')
            break
        else :
            if a*a+b*b==c*c:
                print('是直角三角形')
                break
            else :
                print('是普通三角形')
                break
if a+b<c:
    print('不是三角形')
'''
'''替换
a=56
b=78
i=a
a=b
b=i
print(a,b)
'''
'''密码
i=0
username='root'
userpassword='admin'
while i<3:
    password=input('输入密码')
    if password==userpassword:
        print('密码正确，登陆成功')
        break
    else :
        print('账号密码不匹配')
        i=i+1
else :
    print('密码以连续输入错误三次')
'''
'''三角形
for i in range(8):
    for j in range(0, 8 - i):
        print(end=" ")
    for k in range(8-i,8):
        print('*',end=" ")
    print("")
'''



'''
for i in range(8):
    print(i)
    end= 表示添加一个空字符串，语句没结束
'''
'''99乘法
i=1
while i<=9:
    j = 1
    while j<=i:
        print('%d*%d=%d '%(i,j,i*j),end='')
        j=j+1
    print('')
    i=i+1
'''
'''99乘法
i=9
while i>=1:
    j=1
    while j<=i:
        print('%d*%d=%d '%(i,j,i*j),end='')
        j=j+1
    print('')
    i=i-1
'''
'''青蛙
meter=0
day=0
while meter<20:
    meter=meter+3
    day = day + 1
    if meter>20:
        break
    else :
        meter=meter-2
print(day)
'''
'''阶乘
i=0
s=0
t=1
for i in range(1,21):
    t=t*i
    s=s+t
print(s)
'''


















