"""
    Sandbox program for running python stuff directly.
    <p>
    Only intended to be run via a Python interpreter.

    @author Zimon Kuhs
    @date 2021-09-06
"""

import language.cipher as cipher

text = "I would hesitate, if not at all {0}-wonkiness."

ciphered = cipher.shiftString(text, 5)
print(cipher.shiftString(ciphered, -5))
