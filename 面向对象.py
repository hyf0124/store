'''
class cup:
    high = 0
    v = 0
    color = ''
    material = ''

    def run(self):
        print(self.high,'厘米的',self.material,'材质的杯子可以存放液体')

c = cup()


c.high = 15
c.v = 500
c.color = '透明'
c.material = '玻璃'

c.run()
'''



'''
class computer:
    LED = 0
    price = 0
    cpu = ''
    memory = ''
    hour = 0

    def time(self):
        print('待机了',self.hour,'小时的笔记本电脑打了',self.hour,'小时的字')

    def play(self,playname):
        print(self.LED,'英寸',self.price,'元的，型号为',self.cpu,'内存大小为',self.memory,'待机时长',self.hour,'小时的笔记本电脑打',playname,'非常爽')

    def watch(self,video):
        print(self.LED,'英寸',self.price,'元的，型号为',self.cpu,'内存大小为',self.memory,'待机时长',self.hour,'小时的笔记本电脑在看',video)


c = computer()


c.hour = 72
c.price = 7000
c.cpu = '3060'
c.memory = '一个T'
c.LED = 45



c.play('命运二')
c.watch(video='权力的游戏')
c.time()
'''

'''
class air:
    __price = 0
    __brand = ''
    __time = 0

    def setbrand(self,brand):
        self.__brand = brand

    def getbrand(self):
        return self.__brand

    def setprice(self,price):
        if price <= 0:
            print('空调价格不能小于等于0')
        else:
            self.__price = price

    def getprice(self):
        return self.__price

    def settime(self,time):
        if time <= 0:
            print('时间不能小于等于0')
        else:
            self.__time = time
    def gettime(self):
        return self.__time

    def open(self):
        print('空调开机了')


    def close(self,__time):
        print('空调将在',self.__time,'分钟后自动关闭')

    def show(self,__brand,__price):
        print('空调品牌是',self.__brand,'空调价格为',self.__price,'元')

a = air()
a.open()
a.close(a.settime(15))
a.show(a.setbrand('格力'),a.setprice(123456))
'''


'''
class People:
    __name = ''
    __gender = ''
    __age = 0
    __cost = 0   
    __brand = ''   
    __battery = 0  
    __size = 0    
    __standby = 0   
    __integral = 0  
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setAge(self, age):
        if age <= 0 or age >= 120:
            print('年龄非法！')
        else:
            self.__age = int(age)

    def getAge(self):
        return self.__age

    def setCost(self, cost):
        self.__cost = float(cost)

    def getCost(self):
        return self.__cost

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setBattery(self, battery):
        if battery < 0:
            print('电池容量不能为负！')
        else:
            self.__battery = float(battery)

    def getBattery(self):
        return self.__battery

    def setSize(self, size):
        if size <= 0:
            print('屏幕大小输入非法！')
        else:
            self.__size = int(size)

    def getSize(self):
        return self.__size

    def setStandby(self,standby):
        self.__standby = int(standby)

    def getStandby(self):
        return self.__standby

    def setIntegral(self, integral):
        if integral < 0:
            print('积分不能为负！')
        else:
            self.__integral = int(integral)

    def getIntegral(self):
        return self.__integral

    def show(self):
        print('姓名', self.__name, '\n性别', self.__gender, '\n年龄', self.__age,'\n所拥有的手机剩余话费',
              self.__cost, '元！\n手机品牌', self.__brand,'\n手机电池容量', self.__battery, '%\n屏幕大小',
              self.__size, '寸\n最大待机时长',self.__standby, '分钟\n所拥有积分：', self.__integral)


p = People()
p.setName(input('输入姓名'))
p.setGender(input('输入性别'))
p.setAge(int(input('输入年龄')))
p.setCost(float(input('输入手机剩余话费')))
p.setBrand(input('输入手机品牌'))
p.setBattery(float(input('输入电池容量')))
p.setSize(int(input('输入手机屏幕大小')))
p.setStandby(int(input('输入手机最大待机时长')))
p.setIntegral(int(input('输入拥有积分')))
p.show()
cc = p.getCost()
dd = p.getIntegral()

while True:
    a = int(input('需要打电话还是发短信：（1或2）'))
    if a == 1:
        a_1 = input('输入短信内容：')
        print('短信内容为：\n', a_1)
    elif a == 2:
        a_1 = int(input('输入电话号码：'))
        a_2 = int(input('输入打多长时间：'))
        if a_1 == None: print('不能为空！')
        elif a_1 <= 1: print('电话费不够了！')
        else:
            print('电话已拨通！')
        if a_2 >= 0 and a_2 <= 10:
            if dd >= a_2 * 15:
                dd -= a_2 * 15
            else:
                cc -= a_2 * 1
        elif a_2 > 10 and a_2 <=20:
            if dd >= a_2 * 39:
                dd -= a_2 * 39
            else:
                cc -= a_2 * 0.8
        else:
            if dd >= a_2 * 48:
                dd -= a_2 * 48
            else:
                cc -= a_2 * 0.65

        print('剩余话费为：', cc)
        print('剩余积分为：', dd)
'''

'''
class student:
    __name = ''
    __age = ''

    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self,age):
        if age > 120 or age < 0:
            print('您输入的年龄非法')
        else:
            self.__age = age


    def getage(self):
        return self.__age


    def show(self):
        print('大家好，我叫',self.__name,'，今年',self.__age,'岁了')

    def compare(self,classmate):
        if self.__age > classmate.getage():
            print('我比',classmate.__name,'大',(self.__age - classmate.getage()),'岁')
        elif self.__age < classmate.getage():
            print(self.__name,'比',classmate.__name,'小',(classmate.getage() - self.__age),'岁')
        else:
            print('我俩一样大')

s = student()
s.setname('飞')
s.setage(21)

s1 = student()
s1.setname('关欣')
s1.setage(19)


s.compare(s1)
s1.compare(s)
'''

'''
class student:
    studentnum = 0
    name = ''
    age = 0
    sex = ''
    high = 0
    weight = 0
    achievement = 0
    address = ''
    phonenum = 0

    def show(self):
        print('我叫',self.name,'来自',self.address,self.age,'岁，性别',self.sex,'学号是',self.studentnum,'身高',self.high,'体重',self.weight,'电话号码是',self.phonenum)

    def learn(self,time):
        print(self.name,'已经学习了',time,'小时了')

    def program(self,line):
        print(self.name,'已经打了',line,'行代码了')

    def play(self,gamename):
        print(self.name,'正在玩',gamename)

    def summation(self,*a):
        print(sum(a))
        return a


s = student()
s.name = 'Jarvis'
s.studentnum = 201843310324
s.age = 20
s.sex = '男'
s.high = 178
s.weight = 135
s.achievement = 100
s.address = '宇宙银河系地球亚洲中国'
s.phonenum = 18034275926
s.play('命运二')
s.learn(20)
s.program(500)
s.show()
s.summation(10,10)
'''



'''
class car:
    model = ''
    wheels = 0
    color = ''
    weight = ''
    fuel  = 0



    def run(self,a,b):
        print(self.model,a.model,b.model,'在一起越野')


    def runfast(self,c,d):
        print(self.model,c.model,d.model,'在一起赛车')

c = car()
c.model = '法拉利'
c.color = '镭射'
c.wheels = 4
c.weight = 1300
c.fuel = 50

c1 = car()
c1.model = '宝马'
c1.color = '白色'
c1.wheels = 4
c1.weight = 1600
c1.fuel = 50

c3 = car()
c3.model = '铃木'
c3.color = '黑色'
c3.wheels = 4
c3.weight = 1600
c3.fuel = 50

c4 = car()
c4.model = '五菱'
c4.color = '激光'
c4.wheels = 4
c4.weight = 1800
c4.fuel = 100

c5 = car()
c5.model = '拖拉机'
c5.color = '土黄色'
c5.wheels = 4
c5.weight = 2000
c5.fuel = 200


c3.run(c4,c5)
c.runfast(c1,c4)
'''


'''
class monkey:
    def __init__(self, kind, sex, col, wt):
        self.kind = kind
        self.sex = sex
        self.col = col
        self.wt = wt

    def playgames(self, gamename):
        print(f'{self.col}的{self.sex}{self.kind}正在用{gamename}生火!')

    def work(self, *thing):
        print(f'{self.col}的{self.sex}{self.kind}在学习{thing}')


m = monkey('山顶洞人', '雄性', '金色', '46kg')
m.playgames('打火机')
m.work('python' ' java' ' c++')
'''





































