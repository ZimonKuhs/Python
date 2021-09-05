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


""" ************************** """
""" Temporary ciphering place. """
""" ************************** """

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print("Usage: python cipher.py <word>")
        sys.exit(1)

    key1 = 13
    key2 = 2
    key3 = -1

    scrambled = scramble(sys.argv[1])
    newWord = ""

    for i in range(0, len(scrambled)) :
        digit = ord(scrambled[i]) - 64
        newDigit = digit + (key1 + pow(key2, i)) * pow(key3, i)
        newAscii = 65 + newDigit % 25
        print(newAscii)
        newWord += chr(newAscii)

    oldWord = ""
    for i in range(0, len(scrambled)) :
        ascii = ord(scrambled[i])
        oldChar = chr(65 + (ascii - (key1 + pow(key2, i)) * pow(key3, i)) % 25)
        oldWord += oldChar

    print(newWord)
    print(oldWord)
    sys.exit(0)
