from unittest import TestCase
from Calc import  Calc

class TestCalc(TestCase):

    def testMulti1(self):
        num1 = 10
        num2 = 10
        sum = 100

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMulti2(self):
        num1 = 5
        num2 = 5
        sum = 25

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMulti3(self):
        num1 = 10
        num2 = 10
        sum = 101

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testMulti4(self):
        num1 = 100
        num2 = 10000
        sum = 1000000

        calc = Calc()
        s = calc.multi(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)