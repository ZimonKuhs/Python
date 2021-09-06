"""
    Ciphering functions.

    @author:  Zimon Kuhs.
    @date:    2021-08-18.
"""

import sys

from words import scramble

"""
    Ciphers a string using letter displacemenet via a number.

    TODO: Currently only operates with capital letters.

    @param word     The string to cipher.
    @return         The randomized list.
"""
def caesarCipher(word, key) :
    if not isinstance(word, str) :
        raise Exception("Can only cipher an instance of string (got %s)." % type(word))

    return "".join([char(64 + (int(char) + key) % 25) for char in word])

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
