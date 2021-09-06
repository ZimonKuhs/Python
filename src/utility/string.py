"""
    Utility functionality regarding strings.

    @author:  Zimon Kuhs.
    @date:    2021-07-31.
"""

import math

"""
    Checks whether or not an object's string representation constitutes a palindrome.

    @param object   The object which string representation to check against.
    @return         True if the object's string representation is a palindrome.
"""
def isPalindrome(object) :
    asString = str(object)
    length = len(asString)

    for i in range(0, math.ceil(length / 2)) :
        if asString[i] != asString[length - 1 - i] :
            return False
    return True

"""
    Checks whether or not a character is alphabetical.

    @param matrix  The character to check.
    @return        True if the character is alphabetical.
"""
def isAlphaChar(char) :

    if (char < 'A') :
        return False
    if (char > 'z') :
        return False
    if (char < 'a' and char > 'Z') :
        return False

    return True
