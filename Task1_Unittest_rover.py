'''
    Student shall write their names here
        1. Student 1
        2. Student 2
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


    # Example test case to check lower case rover
    def test_enrove_small(self):
        self.assertEqual(self.rv.enrove('b'), 'bob')

    # You can continue writing your test cases here based on the assignment description

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
        pass

if __name__ == '__main__':
    print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity = 2)