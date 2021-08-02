"""
    Utility functionality regarding strings.

    @author:  Zimon Kuhs.
    @date:    2021-07-31.
"""

import math


def isPalindrome(object) :
    asString = str(object)
    length = len(asString)

    for i in range(0, math.ceil(length / 2)) :
        if asString[i] != asString[length - 1 - i] :
            return True

    return False
