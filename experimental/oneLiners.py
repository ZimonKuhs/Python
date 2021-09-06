"""
    Interesting, cool, or even dumb. As long as it's in a straight line. :)
    <p>

    @author Zimon Kuhs
    @date   2021-09-06
"""


"""
    "Shifts" a character a number of steps in the alphabet, wrapping around at the beginning or end.
    <p>
    Note that captalization is retained.

    @param char     The character to alter.
    @param shift    The alphabetic alteration of the character.
"""
def shiftCharOneLine(char, shift) :
    return char if not ((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')) else \
                chr((65 if char < 'a' else 97) + ((ord(char) - (65 if char < 'a' else 97) + shift) % 26))
