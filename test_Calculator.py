import Calculator
import unittest

class Calc(unittest.TestCase):
    def test_add(self):
        x = 18
        y = 28
        result = Calculator.add(x, y)
        self.assertEqual(result, x+y)

    def test_sub(self):
        x = 18
        y = 12
        result = Calculator.sub(x, y)
        self.assertEqual(result, x-y)

    def test_mul(self):
        x = 12
        y = 10
        result = Calculator.mul(x, y)
        self.assertEqual(result, x*y)

    def test_div(self):
        x = 24
        y = 8
        result = Calculator.div(x, y)
        self.assertEqual(result, x/y)


if __name__=="__main__":
    unittest.main()