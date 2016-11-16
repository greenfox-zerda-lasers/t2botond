from second_exercise import counter
import unittest

class Test2(unittest.TestCase):
    def test_2(self):
        self.assertEqual(counter("fajl.txt"),2)
        self.assertEqual(counter("cdcd"),"No such file")

unittest.main()
