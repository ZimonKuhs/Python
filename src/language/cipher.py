"""
    Ciphering functions.

    @author:  Zimon Kuhs.
    @date:    2021-08-18.
"""

import sys

from utility.string import isAlphaChar

"""
    Ciphers a string using letter displacemenet via a number.

    @param word     The string to cipher.
    @return         The randomized list.
"""
def caesarCipher(word, key) :
    if not isinstance(word, str) :
        raise Exception("Can only cipher an instance of string (got %s)." % type(word))

    return "".join([shiftChar(char, key) for char in word])

"""
    Ciphers a string using a custom conversion function.

    @param word             The string to cipher.
    @param charFunction     The conversion function.
    @param keys             The list of keys to use for each character, with the input function.
"""
def customCipher(word, charFunction, keys) :
    if not isinstance(word, str) :
        raise Exception("Can only cipher an instance of string (got %s)." % type(word))

    if not isinstance(charFunction, function) :
        raise Exception("Can only cipher using a character displacement function (got %s)." % type(charFunction))

    if not isinstance(charFunction, list) or not keys:
        raise Exception("A dict of keys is required in order to cipher a string (got %s)." % keys)

    return "".join([charFunction(char, keys) for char in word])

"""
    "Shifts" a character a number of steps in the alphabet, wrapping around at the beginning or end.
    <p>
    Note that captalization is retained.

    @param char     The character to alter.
    @param shift    The alphabetic alteration of the character.
"""
def shiftChar(char, shift) :

    if not isAlphaChar(char) :
        return char

    base = 65 if char < 'a' else 97
    pos = ord(char) - base
    pos = (pos + shift) % 26

    return chr(base + pos)

"""
    "Shifts" a character a number of steps in the alphabet, wrapping around at the beginning or end.
    <p>
    Note that captalization is retained.
    <p>
    Note that this alternate method exists only because it's fun. It does the same thing as #shiftChar(char, shift)
    but only uses one line of code; less readability, more styling.

    TODO: Find a logical place for shenanigans such as these.

    @param char     The character to alter.
    @param shift    The alphabetic alteration of the character.
"""
def shiftCharOneLine(char, shift) :
    return char if not isAlphaChar(char) else chr((65 if char < 'a' else 97) + ((ord(char) - (65 if char < 'a' else 97) + shift) % 26))

"""
    "Shifts" a character a number of steps in the alphabet, wrapping around at the beginning or end.
    <p>
    Note that captalization is retained.

    @param char     The character to alter.
    @param shift    The alphabetic alteration of the character.
"""
def shiftString(string, shift) :
    pass
