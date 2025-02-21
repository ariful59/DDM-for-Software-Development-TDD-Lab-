'''
    Student shall write their names here
        1. Md Ariful Amin
        2. Sakshi Khanduri
'''

import unittest
from collections import Counter

from Task2 import TextProcessor

class TestTextProcessor(unittest.TestCase):
    tp = None
    tp1 = None
    tp2 = None
    tp3 = None
    tp4 = None
    tp5 = None
    tp6 = None
    tp7 = None
    tp8 = None
    tp9 = None

    def setUp(self):
        self.sample_text = "Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com."
        self.tp = TextProcessor(self.sample_text)

        self.sample_text1 = "PyThOn iS AwEsOmE"
        self.tp1 = TextProcessor(self.sample_text1)

        self.sample_text2 = "Python is great, Python is fun, and Python is everywhere."
        self.tp2 = TextProcessor(self.sample_text2)

        self.sample_text3 = "user@@gmail..com"
        self.tp3 = TextProcessor(self.sample_text3)

        self.sample_text4 = "Check out #Python and #AI. Follow #Python for updates!"
        self.tp4 = TextProcessor(self.sample_text4)

        self.sample_text5 = "Visit https://www.google.com and https://www.example.com for more info."
        self.tp5 = TextProcessor(self.sample_text5)

        self.sample_text6 = "Python is great, Python is fun, and Python is everywhere. Me, me, me!"
        self.tp6 = TextProcessor(self.sample_text6)

        self.sample_text7 = "I have 2 apples and 3 bananas312"
        self.tp7 = TextProcessor(self.sample_text7)

        self.sample_text8 = "This comes under top 10 people. And I have 1,0 points."
        self.tp8 = TextProcessor(self.sample_text8)

        self.sample_text9 = "This is just no numbers"
        self.tp9 = TextProcessor(self.sample_text9)


    def test_convert_to_lowercase(self):
        self.assertEqual(self.tp.convert_to_lowercase(), self.sample_text.lower())

    def test_convert_to_lowercase_with_mix_values(self):
        self.assertEqual(self.tp1.convert_to_lowercase(), self.sample_text1.lower())

    def test_convert_to_lowercase_with_different_text(self):
        self.assertEqual(self.tp2.convert_to_lowercase(), self.sample_text2.lower())

    def test_email_address_extractor (self):
        expected_emails = ["user@example.com"]
        self.assertEqual(self.tp.extract_email_addresses(), expected_emails)

    def test_wrong_email(self):
        self.assertEqual(self.tp3.extract_email_addresses(),[])

    def test_count_unique_hashtag_words(self):
        expected_unique_hashtags = Counter({"#python", "#nlp"})
        self.assertEqual(self.tp.count_unique_hashtag_words(), expected_unique_hashtags)

    def test_count_unique_words_with_different_hashtags(self):
        expected = Counter({'#python': 2, '#ai': 1})
        self.assertEqual(self.tp4.count_unique_hashtag_words(), expected)

    def test_unique_different_urls(self):
        expected = ['https://www.google.com', 'https://www.example.com']
        actual_urls = self.tp5.unique_urls()
        for expected, actual in zip(expected, actual_urls):
            self.assertIn(expected, actual)

    def test_average_word_length(self):
        expected_average_word_length = 6
        self.assertEqual(self.tp.average_word_length(), expected_average_word_length)

    def test_top_three_most_frequent_words(self):
        expected_top_three_most_frequent_words = Counter({'is': 3, 'python': 3, 'hello': 1})
        self.assertEqual(self.tp.top_three_most_frequent_words(), expected_top_three_most_frequent_words)

    def test_top_three_most_frequent_words_with_different_text(self):
        expected = Counter({'python': 3, 'is': 3, 'me': 3})
        self.assertEqual(self.tp6.top_three_most_frequent_words(), expected)

    def test_longest_word(self):
        expected_longest_word = 'programming'
        self.assertEqual(self.tp.longest_word(), expected_longest_word)

    def test_identify_specific_sentences(self):
        expected_identify_specific_sentences = ['Python is awesome.',
                                                'The Python programming language is widely used.',
                                                '#Python #NLP Check out https://example.']
        self.assertEqual(self.tp.identify_specific_sentences(), expected_identify_specific_sentences)

    def test_remove_special_characters(self):
        expected_remove_special_characters = 'Hello This is a sample text 1 Contact me at userexamplecom Python is awesome The Python programming language is widely used Python NLP Check out httpsexamplecom'
        self.assertEqual(self.tp.remove_special_characters(), expected_remove_special_characters)

    def test_replace_digits(self):
        expected_replace_digits = 'Hello! This is a sample text one. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com.'
        self.assertEqual(self.tp.replace_digits(), expected_replace_digits)

    def test_replace_digits_with_different_text(self):
        expected = "I have two apples and three bananasthreeonetwo"
        self.assertEqual(self.tp7.replace_digits(), expected)

    def test_edge_case_with_10(self):
        expected = "This comes under top ten people. And I have one,zero points."
        self.assertEqual(self.tp8.replace_digits(),expected)

    def test_no_numbers(self):
        expected = "This is just no numbers"
        self.assertEqual(self.tp9.replace_digits(),expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
