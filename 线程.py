import threading
from threading  import Thread

lock = threading.Lock()
basket = 0



import time
class cooker1(Thread):
    count = 0
    cooker = ''
    def run(self) -> None:
        global basket

        while True:
            if basket >= 500:
                print('篮子已经满了')
                time.sleep(10)
            else:
                with lock:
                    self.count = self.count + 1

                    basket = basket + 1
                    print('篮子有', self.count, '个')




class customer(Thread):
    money = 3000
    customer1 = ''
    def run(self) -> None:
        global basket
        global money
        while True:
                if basket > 0:
                    with lock:
                        self.money = self.money - 2
                        basket = basket - 1
                        print(self.customer1,'买了一个')
                if self.money == 0:
                    print('钱不够')
                    break

                else:
                    if basket == 0:
                        time.sleep(2)






c1 = cooker1()
c2 = cooker1()
c3 = cooker1()
c4 = customer()
c5 = customer()
c6 = customer()
c7 = customer()
c8 = customer()
c9 = customer()


c1.cooker = 'cc'
c2.cooker = 'dd'
c3.cooker = 'bb'
c4.customer1 = 'aa'
c5.customer1 = 'ee'
c6.customer1 = 'ff'
c7.customer1 = 'qq'
c8.customer1 = 'ww'
c9.customer1 = 'tt'


c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
c7.start()
c8.start()
c9.start()