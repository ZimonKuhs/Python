"""
    Ciphering functions.

    @author:  Zimon Kuhs.
    @date:    2021-08-18.
"""

def caesarCipher(word, key) :
    if not isinstance(word, str) :
        raise Exception("Can only cipher an instance of string (got %s)." % type(word))

    return "".join([char(int(char) + key) for char in word])
