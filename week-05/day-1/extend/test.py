import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass
#Add
    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)

    def test_add_5_and_3_is_8(self):
        self.assertEqual(extend.add(5, 3), 8)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

#MaX of

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 4, 5), 5)

    def test_max_of_three_second(self):
        self.assertEqual(extend.max_of_three(8, 9, 7), 9)

#Median

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)

    def test_median_five2(self):
        self.assertEqual(extend.median([1,1,3,2,2]), 2)

    def test_median_four2(self):
        self.assertEqual(extend.median([9,8,7,1]), 7.5)

    def test_median_one(self):
        self.assertEqual(extend.median([1]), 1)

#vovel

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_is_vovel_u1(self):
        self.assertTrue(extend.is_vovel('Ű'))

    def test_is_vovel_T(self):
        self.assertEqual(extend.is_vovel('T'), None)

    def test_is_vovel_J(self):
        self.assertEqual(extend.is_vovel('J'), None)

    def test_is_vovel_Awe(self):
        self.assertEqual(extend.is_vovel('Awe'), TypeError)

#Tevetranslate

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_avauvutovo(self):
        self.assertEqual(extend.translate('auto'), 'avauvutovo')

if __name__ == '__main__':
    unittest.main()
