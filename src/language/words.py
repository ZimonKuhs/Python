"""
    Functions used for word (~fun~) management.

    @author:  Zimon Kuhs.
    @date:    2021-08-18.
"""

from random import *

"""
    Scrambles an object (currently only lists or strings).

    TODO: Extend to cover other types?

    @param word     The object to scramble.
    @return         The scrambled object.
"""
def scramble(word) :
    function = {
            str : scrambleString,
            list  : scrambleArray
        }[type(word)]

    if function is None :
        raise Exception("%s is not a word." % word)

    return function(word)

"""
    Creates a new list containing the same elements as in the input, but scrambled.

    @param array    The array of objects to scramble.
    @return         The randomized list.
"""
def scrambleArray(array) :
    chars = array.copy()

    result = []
    while chars :
        result.append(chars.pop(randint(0, len(chars) - 1)))

    return result

"""
    Returns an anagram of a string.

    TODO: Probably not too optimized...

    @param word     The original string to scramble.
    @return         A randomized anagram of the input.
"""
def scrambleString(word) :
    return "".join(scrambleArray([char for char in word]))
