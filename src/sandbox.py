"""
    Sandbox program for running python stuff directly.
    <p>
    Only intended to be run via a Python interpreter.

    @author Zimon Kuhs
    @date 2021-09-06
"""

text = ""
for i in range(0, 26) :
    text += chr(65 + i) + chr(97 + i)

print(text)
