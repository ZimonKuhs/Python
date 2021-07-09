"""
@author:  Zimon Kuhs.
@date:    2021-07-08.

TODO:   Anagram logic should be moved, or wordReader renamed.
        Optimize using sets? I.e. build key->set chains with words' characters.
"""

import json
from utility import absolutePath

JSON_FILE = absolutePath(__file__, "./data/words.json")

with open(JSON_FILE) as file:
    words = json.load(file)

"""
    Checks whether a string is a word or not.

    @param word    The string to check.
    @return        True if the string can be found in the dictionary.
"""
def isWord(word):
    return word in words

"""
    Finds all anagrams of a string.

    @param phrase    The string to find anagrams of.
    @return          A list of words which are anagrams of the input string.
"""
def anagrams(phrase):
    if (len(phrase) <= 0):
        return []

    return [word for word in words if isAnagram(word, phrase)]

"""
    Checks whether or not a word is a character subset of a set of characters.

    @param word      The word to check.
    @param phrase    The set of characters to check against.
    @return          True if the word is an anagram of the string.
"""
def isAnagram(word, phrase):
    if (len(word) <= 0):
        return True
    if (len(word) > len(phrase)):
        return False

    phraseChars = [char for char in phrase]
    wordChars = [char for char in word]

    while wordChars:
        char = wordChars.pop(0)

        if char not in phraseChars:
            return False

        phraseChars.remove(char)

    return True