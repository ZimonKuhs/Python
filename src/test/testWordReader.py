"""
@author:  Zimon Kuhs.
@date:    2021-07-08.
"""

import json
import random
import unittest

from language import wordReader as reader
from utility import absolutePath, alphabeticCharacters, randomWord

alphaNumeric = [char for char in (alphabeticCharacters())]
alphaNumericLength = len(alphaNumeric)

class TestWordReader(unittest.TestCase):
    """
        This test class reads the word file separately to cover the case where
        language.wordReader itself would be reading it erroneously.

        Attributes:
            amount(int):  The number of words in the dictionary.
            words (list): The dictionary's words.
    """
    with open(absolutePath(__file__, "../language/data/words.json")) as file:
        words = list(json.load(file).keys())
        amount = len(words)

    def __init__self(self):
        pass

    """
        Verify positive cases for isWord(str).

        Implicitly tests that wordReader can read its base file.
    """
    def testIsWord(self):
        for word in self.words:
            self.assertTrue(reader.isWord(word), "%s was erroneously identified as a non-word." % word)

    """
        As the amount of possible non-word strings is infinite, this test
        utilizes randomly generated strings as a monkey test.
    """
    def testNotWords(self):
        x = 0

        while x < 10:
            nonWord = randomWord(random.randint(1, 25))

            if nonWord not in self.words:
                x += 1
                self.assertFalse(reader.isWord(nonWord), "%s was erroneously identified as a word." % str)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
