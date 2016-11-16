from first_exercise import divider
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(divider(0),"fail")
        self.assertEqual(divider(1),10)

unittest.main()
