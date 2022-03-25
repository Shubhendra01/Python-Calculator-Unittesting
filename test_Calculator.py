import Calculator
import unittest

class Calc(unittest.TestCase):

    def setUp(self):
        self.x = 88
        self.y = 78
    def tearDown(self):
        self.x = 0
        self.y = 0

    def test_add(self):

        result = Calculator.add(self.x, self.y)
        self.assertEqual(result, self.x+self.y)

    def test_sub(self):

        result = Calculator.sub(self.x, self.y)
        self.assertEqual(result, self.x-self.y)

    def test_mul(self):

        result = Calculator.mul(self.x, self.y)
        self.assertEqual(result, self.x*self.y)

    def test_div(self):

        result = Calculator.div(self.x, self.y)
        self.assertEqual(result, self.x/self.y)


if __name__=="__main__":
    unittest.main()