"""
@author:  Zimon Kuhs.
@date:    2021-07-08.
"""

import json
from utility import absolutePath

JSON_FILE = absolutePath(__file__, "./data/words.json")

with open(JSON_FILE) as file:
    words = json.load(file)

"""
    Checks whether a string is a word or not.

    @param word    The string to check.
"""
def isWord(word):
    return word in words

"""
    Finds all words that are subsets of a collection of characters.

    @param characters    The characters with which to find subsets.
"""
def subsets(characterString):
    if (len(characterString) <= 0):
        return []

    return [word for word in words if isSubsetOf(word, characterString)]

def isSubsetOf(word, characterString):
    if (len(word) <= 0):
        return True
    if (len(word) > len(characterString)):
        return False

    characters = [char for char in characterString]
    wordChars = [char for char in word]

    while wordChars :
        char = wordChars.pop(0)

        if char not in characters:
            return False

        characters.remove(char)

    return True