import unittest
import code_sample


class TestDecideAlphabet(unittest.TestCase):

    def test_decide_alphabet_1(self):
        """Base case: english alphabet"""
        alphabetical_words = [
            "aaa",
            "aac",
            "aba",
            "bab",
            "bac",
            "bba",
            "caa"
        ]
        # expected alphabet = ['a', 'b', 'c']

        resulting_alphabet = code_sample.decide_alphabet(alphabetical_words)

        self.assertEqual(resulting_alphabet, ['a', 'b', 'c'])


    def test_decide_alphabet_2(self):
        """test case: non english alphabet"""
        alphabetical_words = [
            "bac",
            "aaa",
            "acb"
        ]
        # expected alphabet = ['b', 'a', 'c']

        resulting_alphabet = code_sample.decide_alphabet(alphabetical_words)

        self.assertEqual(resulting_alphabet, ['b', 'a', 'c'])


    def test_decide_alphabet_3(self):
        """test case: non english alphabet with different characters"""
        alphabetical_words = [
            "+!$!",
            "+$!",
            "!!!",
            "!$$",
            "$$+"
        ]
        # expected alphabet = ['+', '!', '$']

        resulting_alphabet = code_sample.decide_alphabet(alphabetical_words)

        self.assertEqual(resulting_alphabet, ['+', '!', '$'])


    def test_decide_alphabet_empty(self):
        """edge case: no words"""
        alphabetical_words = []
        # expected alphabet = []

        resulting_alphabet = code_sample.decide_alphabet(alphabetical_words)

        self.assertEqual(resulting_alphabet, [])


    def test_decide_alphabet_one_word(self):
        """edge case: only one word"""
        alphabetical_words = ['aafasflasf']
        # expected alphabet = []

        resulting_alphabet = code_sample.decide_alphabet(alphabetical_words)

        self.assertEqual(resulting_alphabet, [])
        

if __name__ == '__main__':
    unittest.main()