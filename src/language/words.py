"""
    Functions used for word (~fun~) management.

    @author:  Zimon Kuhs.
    @date:    2021-08-18.
"""

def scramble(word) :
    function = {
        "string" : scrambleString,
        "array"  : scrambleArray
        }[type(word)]

    if function is None :
        raise Exception("%s is not a word." % word)

    return function(word)

def scrambleArray(word) :
    return None

def scrambleString(word) :
    return None
