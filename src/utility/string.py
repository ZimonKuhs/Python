"""
    Utility functionality regarding strings.

    @author:  Zimon Kuhs.
    @date:    2021-09-06.
"""

"""
    Checks whether or not a character is alphabetical.

    @param matrix  The character to check.
    @return        True if the character is alphabetical.
"""
def isAlphaChar(char) :

    if (char < 'A') :
        return False
    if (char > 'z') :
        return False
    if (char < 'a' and char > 'Z') :
        return False

    return True
