"""
    'Largest Palindrome Product'

    https://projecteuler.net/problem=4

    @author:    Zimon Kuhs
    @date:      2021-07-30
    @solution:  906609
"""

import math
import sys

from utility import math as mathUtility
from utility import string as stringUtility

#  TODO:   Move to a JSON configuration file.
THRESHOLD = 5

"""
    Finds the largest palindrome number* from the product of n-number digits, n being the number of digits.

    * A palindrome number is analogous to a textual palindrome; its sequence is equivalent to its inverted sequence.

    @param length   The length of the palindrome numbers to consider.
    @return         The largest palindrome number that is a product of two numbers of the specified length.
"""
def solve(length):
    if not mathUtility.isPositiveInteger(length):
        raise Exception("Input number must be a positive, non-zero integer!")

    if length > THRESHOLD:
        raise Exception("Input number length is too large, %d is the maximum allowed number; %d was supplied." % (THRESHOLD, length))

    palindromes = findPalindromes(length)

    highest = - sys.maxsize
    for number in palindromes :
        product = number * number
        highest = highest if highest >= product else product

    return product

"""
    Retrieves all palindrome numbers of a specified length.

    * A palindrome number is analogous to a textual palindrome; its sequence is equivalent to its inverted sequence.

    @param digits   The digit length of palindromes to collect.
    @return         All palindrome numbers of the specified length.
"""
def findPalindromes(digits):
    if digits <= 1 :
        raise Exception("Can not generate palindromes from numbers shorter than 2 digits! Received request for %d digits.", digits)

    result = []
    for i in range(10^digits, int(math.pow(10, digits + 1))) :
        if stringUtility.isPalindrome(i) :
            result.append(i)

    return result
