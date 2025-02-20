import re
from collections import Counter
from math import ceil


class TextProcessor:
    def __init__(self, text):
        self.text = text
    ''' 1. Convert all words to lowercase.'''

    def convert_to_lowercase(self):
        return self.text.lower()

    '''2. Extract all the email addresses mentioned in the text.'''
    def extract_email_addresses(self):
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, self.text)
        return emails if emails else []

    '''  3. Find and count all unique hashtags (words or phrases starting with #) used in the document.'''
    def count_unique_hashtag_words(self):
          hashtag_words = r'#[\w]+'
          hashtags = re.findall(hashtag_words, self.text)
          hashtags = [hashtag.lower() for hashtag in hashtags]
          return Counter(hashtags)

    '''  4. Identify and list all URLs mentioned in the text.'''
    def unique_urls(self):
        url_pattern = r'https?://[^s]+'
        urls = re.findall(url_pattern, self.text)
        return urls

    '''   5. Calculate the average word length in the document.'''
    def average_word_length(self):
        words = self.text.split()
        total_length = sum(len(word) for word in words)
        return ceil(total_length / len(words) if len(words) > 0 else 0)

    '''    6. Determine the top 3 most frequent words in the text.'''
    def top_three_most_frequent_words(self):
        text = self.remove_special_characters()
        words = text.lower().split()
        top_three_words = Counter(words).most_common(3)
        return Counter(dict(top_three_words))

    '''   7. Find the longest word in the text.'''
    def longest_word(self):
        word_pattern = r'\b\w+\b'
        words = re.findall(word_pattern, self.text)
        longest_word = max(words, key=len)
        return longest_word if len(words) > 0 else ''

    '''    8. Identify the sentences in the document that contain the word "Python.'''
    def identify_specific_sentences(self, keyword = 'Python'):
        word_pattern = rf'([^.?!]*\b{keyword}\b[^.?!]*[.?!])'
        sentences = re.findall(word_pattern, self.text)
        list = [sentences.strip() for sentences in sentences]
        return list

    '''    9. Remove all punctuation and special characters from the text.'''
    def remove_special_characters(self):
         return re.sub(r'[^a-zA-Z0-9\s]', '', self.text)

    '''    10. Convert all numerical figures (1-10) within the text into their respective written out forms
     (for example, “This is sample text 1, 2, 3” shall become “This is sample text one, two, three”).'''

    def replace_digits(self):
        number_map = {
            "0":"zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
            "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"
        }
        return re.sub(r'(10|[0-9])', lambda m: number_map[m.group()], self.text)

# email = "user@@gmail..com"
# tp = TextProcessor(email)
# print(tp.extract_email_addresses())