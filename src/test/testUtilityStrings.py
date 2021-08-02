"""
    Regression tests array utility functions.

    @author:  Zimon Kuhs.
    @date:    2021-07-12.
"""

import unittest

import utility.string as strings

"""
    Verifies that all string utility functionality is correct.
"""
class TestEuler(unittest.TestCase):
    """
        Nothing spanning all tests is necessary to set up for the instance.
    """
    def __init__self(self):
        pass

    """
        Check that a palindrome can be correctly identified.
    """
    def testIsPalindrome(self):
        self.assertTrue(strings.isPalindrome("abcdefghhgfedcba"))
        self.assertTrue(strings.isPalindrome("tacocat"))
        self.assertFalse(strings.isPalindrome("just me all along"))
        self.assertTrue(strings.isPalindrome(""))

    def testNonStringPalindrome(self):
        self.assertFalse(strings.isPalindrome(112))
        self.assertTrue(strings.isPalindrome(121))
        self.assertFalse(strings.isPalindrome(0.123321))
        self.assertFalse(strings.isPalindrome(0.12210))
        self.assertFalse(strings.isPalindrome({"a": "b", "b": "a"}))
        self.assertFalse(strings.isPalindrome([1, 2, 3, 3, 3, 3, 3]))
        self.assertFalse(strings.isPalindrome([1, 2, 3, 4, 3, 2, 1]))

if __name__ == "__main__":
    unittest.main()
