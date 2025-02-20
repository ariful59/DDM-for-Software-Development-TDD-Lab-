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
    def setUp(self):
        self.sample_text = ("Hello! This is a sample text 1. Contact me at user@example.com. Python is awesome. The Python programming language is widely used. #Python #NLP Check out https://example.com."
                            "The top 3 programming languages are: 1. Python 2. Java 3. C++.")
        self.tp = TextProcessor(self.sample_text)

    def test_convert_to_lowercase(self):
        self.assertEqual(self.tp.convert_to_lowercase(), self.sample_text.lower())

    def test_convert_to_lowercase_with_different_text(self):
        text = "Python is great, Python is fun, and Python is everywhere."
        tp = TextProcessor(text)
        expected = "python is great, python is fun, and python is everywhere."
        self.assertEqual(tp.convert_to_lowercase(), expected)

    def test_email_address_extractor (self):
        expected_emails = ["user@example.com"]
        self.assertEqual(self.tp.extract_email_addresses(), expected_emails)

    def test_count_unique_hashtag_words(self):
        expected_unique_hashtags = Counter({"#python", "#nlp"})
        self.assertEqual(self.tp.count_unique_hashtag_words(), expected_unique_hashtags)

    def test_count_unique_words_with_different_hashtags(self):
        text = "Check out #Python and #AI. Follow #Python for updates!"
        tp = TextProcessor(text)
        expected = Counter({'#python': 2, '#ai': 1})
        self.assertEqual(tp.count_unique_hashtag_words(), expected)

    def test_unique_urls(self):
        expected_unique_urls = ["https://example.com."]
        actual_urls = self.tp.unique_urls()
        for expected, actual in zip(expected_unique_urls, actual_urls):
            self.assertEqual(expected, actual)

    def test_unique_different_urls(self):
        text = "Visit https://www.google.com and https://www.example.com for more info."
        tp = TextProcessor(text)
        expected = ['https://www.google.com', 'https://www.example.com']
        actual_urls = tp.unique_urls()
        for expected, actual in zip(expected, actual_urls):
            self.assertIn(expected, actual)

    def test_average_word_length(self):
        expected_average_word_length = 6
        self.assertEqual(self.tp.average_word_length(), expected_average_word_length)

    def test_top_three_most_frequent_words(self):
        expected_top_three_most_frequent_words = Counter({'is': 3, 'python': 3, 'hello': 1})
        self.assertEqual(self.tp.top_three_most_frequent_words(), expected_top_three_most_frequent_words)

    def test_top_three_most_frequent_words_with_different_text(self):
        text = "Python is great, Python is fun, and Python is everywhere. Me, me, me!"
        tp = TextProcessor(text)
        expected = Counter({'python': 3, 'is': 3, 'me': 3})
        self.assertEqual(tp.top_three_most_frequent_words(), expected)

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
        text = "I have 2 apples and 3 bananas312"
        tp = TextProcessor(text)
        expected = "I have two apples and three bananasthreeonetwo"
        self.assertEqual(tp.replace_digits(), expected)




if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
