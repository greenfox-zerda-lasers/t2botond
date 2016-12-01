import unittest
import filename4

class TestExam(unittest.TestCase):
    def setUp(self):
        pass

    def testgreeter0(self):
        self.assertEqual(filename4.greeter('X'), 'Hello, X!')

    def testgreeter1(self):
        self.assertEqual(filename4.greeter(''), 'Hello, Mr Nobody!')


if __name__ == '__main__':
    unittest.main()
