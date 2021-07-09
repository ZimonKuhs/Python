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
        This test class reads the word file separately to cover the case where language.wordReader itself would be
        reading it erroneously.

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
        As the amount of possible non-word strings is infinite, this test utilizes randomly generated strings
        (only alphabetical characters) as a monkey test.
    """
    def testNotWords(self):
        x = 0

        while x < 10:
            nonWord = randomWord(random.randint(1, 25))

            if nonWord not in self.words:
                x += 1
                self.assertFalse(reader.isWord(nonWord), "%s was erroneously identified as a word." % str)

    """
        Tests the following cases:

        *    Word is subset of other, longer word.
        *    Word is subset of other, equally long word.
        *    Word is subset of other, longer, non-word.
        *    Word is not subset of other, shorter word.
        *    Word is not subset of other, longer word.
        *    Word is not subset of other, equally long word.
        *    Word is not subset of other, equally long, non-word.

        Also checks for expected behavior when other string is empty.
    """
    def testIsAnagram(self):
        self.assertTrue(reader.isAnagram("clam", "calamity"))
        self.assertTrue(reader.isAnagram("stressed", "desserts"))
        self.assertTrue(reader.isAnagram("iniquity", "abiiinquty"))
        self.assertFalse(reader.isAnagram("malpractice", "acclaimer"))
        self.assertFalse(reader.isAnagram("tuners", "conquest"))
        self.assertFalse(reader.isAnagram("barking", "parking"))
        self.assertFalse(reader.isAnagram("barking", "aagnikra"))

        self.assertTrue(reader.isAnagram("", "asterisk"))
        self.assertFalse(reader.isAnagram("filler", ""))

    """
        Check that the appropriate amount of subset words are collected.
    """
    def testAnagrams(self):
        self.assertEqual(["g", "gl", "gn", "go", "gol", "gon", "l", "lg", "ln", "lo", "log",
                          "long", "n", "ng", "nl", "no", "nog", "nol", "o", "og", "ol", "on"],
                          reader.anagrams("long"),
                         "Subset mismatch for long.")
        self.assertEqual(["a"], reader.anagrams("a"), "Subset of \"a\" is itself.")
        self.assertEqual([], reader.anagrams("!#%&/()=)}"), "Subsets of \"!#%&/()=)}\" shouldn't exist.")
        self.assertEqual([], reader.anagrams(""), "Subsets of nothing should be nothing.")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
