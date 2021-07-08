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