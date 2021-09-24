
'''
class cooker:
    __name = ''
    __age = 0

    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def setage(self,age):
        self.__age = age

    def getage(self):
        return self.__age

    def hotrice(self):
        pass


class apprentice(cooker):
    def cook(self):
        pass


class apprenticeson(apprentice):
    def hotrice(self):
        super().hotrice()
        print('蒸饭')

    def cook(self):
        print('炒菜')

a = apprenticeson()
a.hotrice()
a.cook()
'''



'''
class human:
    age = 0
    sex = ''
    name = ''

    def work(self):
        print(self.age,'岁的',self.name,'还坚持在工地上偷奸耍滑')

    def learn(self):
        print(self.age,'岁的',self.name,'还在坚持学习')

    def sing(self):
        print(self.age,'岁的',self.name,'正在唱歌')

class worker(human):
      def work(self):
          super().work()

class student(human):
      def learn(self):
          super().learn()
      def sing(self):
          super().sing()

w = worker()
w.name = '王师傅'
w.age = 41
w.sex = '男'
w.work()

s = student()
s.age = 20
s.sex = '男'
s.name = '阿飞'
s.learn()
s.sing()
'''

'''
import time
class Oldphone:
    __brand = ''
    def setbrand(self,brand):
        self.__brand=brand
    def getbrand(self):
        return self.__brand
    def call(self, number):
        print(f'正在给打{number}电话')
        for i in range(3):
            print('.', end='')
            time.sleep(1)
        print('已接通')
class newphone(Oldphone):
    def dial(self,number):
        print('语音拨号中...')
        super().call(number)
    def sow(self):
        print(f'品牌为{self.getbrand()}的手机很好用')


n=newphone()
n.setbrand('vivo')
n.dial(input('请输入要拨打的电话号码'))
n.sow()
'''




