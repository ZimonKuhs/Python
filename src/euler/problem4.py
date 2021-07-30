"""
    'Largest Palindrome Product'

    https://projecteuler.net/problem=4

    @author:    Zimon Kuhs
    @date:      2021-07-30
    @solution:  906609
"""

import math

from utility.math import math as utilityMath
from utility.string import string as utilityString

#  TODO:   Move to a JSON configuration file.
THRESHOLD = 5

"""
    Finds the largest palindrome number* from the product of n-number digits, n being the number of digits.

    * A palindrome number is analogous to a textual palindrome; its sequence is equivalent to its inverted sequence.

    @param length   The length of the palindrome numbers to consider.
    @return         The largest palindrome number that is a product of two numbers of the specified length.
"""
def solve(length):
    if not utilityMath.isPositiveInteger(length):
        raise Exception("Input number must be a positive, non-zero integer!")

    if (length > THRESHOLD):
        raise Exception("Input number length is too large, %d is the maximum allowed number; %d was supplied." % (THRESHOLD, length))


    palindromes = findPalindromes(length)

def findPalindromes(digits) {
    # Check digit length, discard all numbers lower than 10^<digits>.
}
