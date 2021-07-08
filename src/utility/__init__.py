"""
@author:  Zimon Kuhs.
@date:    2021-07-08.
"""

import os
import random

ALPHA = [chr(i) for i in range(128)
         if i > 65 and i < 91 or i > 97 and i < 122]
ALPHA_LENGTH = len(ALPHA)

def absolutePath(filePath, relativePath):
    return os.path.join(os.path.dirname(filePath), relativePath)

"""
    Retrieves all of the alphabetic characters in the ASCII table.

    @return: all alphabetic characters.
"""
def alphabeticCharacters():
    return ALPHA.copy()

"""
    Generates a random string.

    @param length  The character length of the string to generate.
    @return        A randomized word.
"""
def randomWord(length):
    result = ""
    for _ in range(0, length):
        result += ALPHA[random.randint(0, ALPHA_LENGTH - 1)]
    return result