'''
    Student shall write their names here
        1. Md Ariful Amin
        2. Sakshi Khanduri
'''

import unittest
from Task2 import TextProcessor

class LowerCaseChecker(unittest.TestCase):
    tp = None
    def setUp(self):
        self.sample_text = "Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com."
        self.tp = TextProcessor(self.sample_text)

    def test_convert_to_lowercase(self):
        self.assertEqual(self.tp.convert_to_lowercase(), self.sample_text.lower())


class EmailAddressExtractor(unittest.TestCase):
    tp = None
    def setUp(self):
        self.sample_text = "Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com."
        self.tp = TextProcessor(self.sample_text)

    def test_email_address_extractor (self):
        expected_emails = ["user@example.com"]
        self.assertEqual(self.tp.extract_email_addresses(), expected_emails)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    """
    To generate an HTML report
    coverage run -a --branch Task1_Unittest_rover.py 
    coverage run -a --branch Task2_unittest.py 
    coverage report -m
    coverage html
    """
