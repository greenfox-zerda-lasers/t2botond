from third_exercise import Person
import unittest

class Test3(unittest.TestCase):
    def test3(self):
        self.assertRaises(ValueError, Person,"Bela",11923)
        person1 = Person("wcdw",1111)
        self.assertEqual(person1.name,"wcdw")
        self.assertEqual(person1.birth_date,1111)
unittest.main()
