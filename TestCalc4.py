from unittest import TestCase
from Calc import  Calc

class TestCalc(TestCase):

    def testDevision1(self):
        num1 = 10
        num2 = 10
        sum = 1

        calc = Calc()
        s = calc.devision(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testDevision2(self):
        num1 = 10
        num2 = 1
        sum = 10

        calc = Calc()
        s = calc.devision(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testDevision3(self):
        num1 = 10
        num2 = 5
        sum = 2

        calc = Calc()
        s = calc.devision(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)

    def testDevision4(self):
        num1 = 10
        num2 = 2
        sum = 2

        calc = Calc()
        s = calc.devision(num1,num2)

        # 判断，断言
        self.assertEqual(sum,s)