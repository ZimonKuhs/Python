"""
    Test suite for regression testing cipher functions.

    @author:  Zimon Kuhs.
    @date:    2021-09-06.
"""

import unittest

import language.cipher as cipher


class TestCipher(unittest.TestCase):
    """
        @attribute upper    All uppercase letters.
        @attribute lower    All lowercase letters.
    """
    upper = [chr(ordinal) for ordinal in range(65, 91)]
    lower = [chr(ordinal) for ordinal in range(97, 123)]

    def testShiftChar(self):
        self.assertEqual('A', cipher.shiftChar('A', 0))
        self.assertEqual('B', cipher.shiftChar('A', 1))
        self.assertEqual('Z', cipher.shiftChar('A', 25))

        self.assertEqual('A', cipher.shiftChar('A', 26))
        self.assertEqual('B', cipher.shiftChar('A', 27))
        self.assertEqual('Y', cipher.shiftChar('A', 50))
        self.assertEqual('Z', cipher.shiftChar('A', 51))

        self.assertEqual('Z', cipher.shiftChar('A', -1))
        self.assertEqual('B', cipher.shiftChar('A', -25))
        self.assertEqual('A', cipher.shiftChar('A', -26))

        self.assertEqual('A', cipher.shiftChar('A', 26 * 10))
        self.assertEqual('B', cipher.shiftChar('A', 1 + 26 * 10))
        self.assertEqual('Z', cipher.shiftChar('A', 25 + 26 * 100))
        self.assertEqual('A', cipher.shiftChar('A', 26 + 26 * 1000))

        self.assertEqual('Z', cipher.shiftChar('A', -1 + 26 * 10))
        self.assertEqual('B', cipher.shiftChar('A', -25 + 26 * 100))
        self.assertEqual('A', cipher.shiftChar('A', -26 + 26 * 1000))

    """
        Tests Caesar cipher with the key being up to twice the length of the alphabet.
        This to ensure that keys of greater length makes the shifting wrap around to
        only alphabetical characters.
    """
    def testCaesar(self):
        originalText = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        expectedText = originalText

        for i in range(0, 52) :
            self.assertEqual(expectedText, cipher.caesarCipher(originalText, i), "Failed for key %d." % i)
            expectedText = expectedText[2:] + expectedText[0:2]

    def testCaesarNegative(self):
        originalText = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        expectedText = originalText

        for i in range(-52, 0) :
            self.assertEqual(expectedText, cipher.caesarCipher(originalText, i), "Failed for key %d." % i)
            expectedText = expectedText[2:] + expectedText[0:2]
