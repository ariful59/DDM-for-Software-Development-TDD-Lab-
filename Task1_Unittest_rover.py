'''
    Student shall write their names here
        1. Md Ariful Amin
        2. Sakshi Khanduri
'''


import unittest
from Task1_Rover import rovar

class test_string(unittest.TestCase):
    '''
        _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
        _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
        Swedish vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

        Write your TCs based on the lab instructions. One TC has been written below as an example
        
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Set up shared resources = Class instance to access rover class methods
        '''
        cls.rv= rovar() 

    # def test_empty_string(self):
    #     self.assertEqual(self.rv.enrove(""),"")

    def test_single_vowel(self):
        self.assertEqual(self.enrove("a"),"a")

    def test_single_consonant(self):
        self.assertEqual(self.enrove("c"),"coc")
    def test_double_consonant(self):
        self.assertEqual(self.enrove('cc'),'coccoc')
    def test_string_with_numbers(self):
        self.assertEqual(self.enrove("h3llo"),"ho3lololo")
    # Example test case to check lower case rover
    def test_enrove_small(self):
        self.assertEqual(self.rv.enrove('b'), 'bob')

    def test_enrove_upper(self):
        self.assertEqual(self.rv.enrove('B'), 'BOB')

    def test_enrove_special(self):
        self.assertEqual(self.rv.enrove('&'), '&')

    def test_enrove_numbers(self):
        self.assertEqual(self.rv.enrove('3'), '3')

    def test_enrove_all_letters(self):
        self.assertEqual(self.rv.enrove('abcö'), 'abobcocö')

    def test_enrove_empty_string(self):
        self.assertEqual(self.rv.enrove(''), '')

    def test_enrove_multiple_chars(self):
        self.assertEqual(self.rv.enrove('Hello!'), 'HOHelollolo!')

    def test_enrove_null(self):
        self.assertEqual(self.rv.enrove(None), None)


    def test_single_vowel(self):
        self.assertEqual(self.rv.derove("a"),"a")

    def test_single_consonant(self):
        self.assertEqual(self.rv.derove("coc"),"c")

    def test_double_consonant(self):
        self.assertEqual(self.rv.derove('coccoc'),'cc')

    def test_string_with_numbers(self):
        self.assertEqual(self.rv.derove("HoH3lololo"),"H3lolo")

    def test_derove_small(self):
        self.assertEqual(self.rv.derove('bob'), 'b')

    def test_derove_upper(self):
        self.assertEqual(self.rv.derove('BOB'), 'B')

    def test_derove_special(self):
        self.assertEqual(self.rv.derove('&'), '&')

    def test_derove_numbers(self):
        self.assertEqual(self.rv.derove('3'), '3')

    def test_derove_all_letters(self):
        self.assertEqual(self.rv.derove('HoHelollolo!'),'Hello!')

    def test_derove_null(self):
        self.assertEqual(self.rv.derove(None), None)

if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity=2, exit=False)