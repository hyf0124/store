print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
import random
bank={}
bank_name="工商银行七马路分行"
#                 一一对应  ，  不是名称对应
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100 :return 3#bank_adduer=3
    if username in bank:return 2#bank_adduer=2
    bank[username]={
        "account": account,#键：你输入的值account=random.randint(10000000,99999999)
        "password": password,# password = input("请输入您的密码")
        "country": country,#country = input("\t\t请输入您的国家")
        "province": province,
        "street": street,
        "door": door,
        "money":0,
        "bank_name":bank_name
    }
    print(bank[username]['password'])
    return 1#bank_adduer=1
def adduser():
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    status=bank_adduser(account,username,password,country,province,street,door)
    if status == 1:
        print("恭喜你开户成功下面是你的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    elif status == 2:
        print('用户已存在')
    elif statue == 3:
        print('用户库已满')



def usermoney():

    username=input('请输入您的用户名')
    money = bank[username]['money']
    appmoney = money
    if username in bank:
        password = input('请输入您的密码')
    else :
        print('账号不存在')
    if password != bank[username]['password']:
        print('密码输入错误')
    else :
        usermoney = int(input('请输入您的取款金额'))
        if usermoney > appmoney:
            print('余额不足')
        else :
            appmoney = appmoney - usermoney
            bank[username]['money']=appmoney
    print(bank[username]['money'])

def amunt():

    username=input('请输入您的用户名')
    amunt=int(input('请输入您要存入的金额'))
    money = bank[username]['money']
    if username in bank:

        money=money + amunt
        bank[username]['money']=money
    print(money)



def transfer():

    username1 = input('请输入付款用户名')

    username2 = input('请输入收款用户名')

    if username1 in bank and username2 in bank and username1 != username2:
            password = input('请输入付款账号密码')
            if password != bank[username1]['password']:
                print('密码错误')
            else :
                    transfer_money = int(input('请输入转账金额'))
                    if transfer_money > bank[username1]['money']:
                        print('余额不足')
                    else:
                        bank[username1]['money'] = bank[username1]['money'] - transfer_money
                        bank[username2]['money'] = bank[username2]['money'] + transfer_money
    print(bank[username1]['money'])
    print(bank[username2]['money'])

def search():
    username=input('请输入用户名')
    password = input('请输入密码')
    if username in bank:
        if password == bank[username]['password']:
            print(bank[username])
        else :
            print('密码错误')
    else:
        print('用户名错误')





while True:
    begin=input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    elif  begin == "2":
        print("2、取钱")
        usermoney()
    elif  begin == "3":
        print("3、存钱")
        amunt()
    elif  begin == "4":
        print("4、转账")
        transfer()
    elif  begin == "5":
        print("5、查询 ")
        search()
    elif  begin == "6":
        print("6、退出")
        break