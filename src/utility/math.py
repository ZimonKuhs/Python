"""
    Utility functionality regarding mathematics.

    TODO:   Move "checking if it's a number to begin with" to its own function.

    @author:  Zimon Kuhs.
    @date:    2021-07-30.
"""

import math

"""
    Checks whether or not an object is an integer.

    @param input    The object to be checked.
    @return         True if the object is indeed an integer.
"""
def isNumber(number):
    return isinstance(number, (int, float, complex)) and not isinstance(number, bool)


"""
    Checks whether or not an object is a positive integer.

    @param input    The object to be checked.
    @return         True if the object is indeed a positive number.
"""
def isPositiveInteger(number):
    return isNumber(number) and number > 0

"""
    Calculates the digit length of a number.

    N.B. Will not regard the minus sign as a digit.

    @param number   The digit whose length to calculate.
    @return         The digit length of the number.
"""
def numberLength(number):
    if not isNumber(number):
        raise Exception("Input number must be a positive, non-zero integer!")

    if number < 0 :
        number = -number

    return int(math.log10(number))+1
