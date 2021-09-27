from unittest import TestCase
from Calc import  Calc

class TestCalc(TestCase):


    def testMinus1(self):
        num1 = 100
        num2 = 50
        sum = 50

        calc = Calc()
        s = calc.minus(num1, num2)

        self.assertEqual(sum, s)


    def testMinus2(self):
        num1 = 105
        num2 = 50
        sum = 55

        calc = Calc()
        s = calc.minus(num1, num2)

        self.assertEqual(sum, s)


    def testMinus3(self):
        num1 = 10
        num2 = 5
        sum = 5

        calc = Calc()
        s = calc.minus(num1, num2)

        self.assertEqual(sum, s)


    def testMinus4(self):
        num1 = 100
        num2 = 150
        sum = 50

        calc = Calc()
        s = calc.minus(num1, num2)

        self.assertEqual(sum, s)