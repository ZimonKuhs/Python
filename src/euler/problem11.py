"""
@author:  Zimon Kuhs.
@date:    2021-07-09.
"""

import functools

def solve(matrix):
    verifyMatrix(matrix)

    return max(
            maxHorizontally(matrix),
            maxVertically(matrix),
            maxDiagonally(matrix)
        )

def maxDiagonally(matrix):
    return 0

def maxHorizontally(matrix):
    return 0

def maxVertically(matrix):
    return 0

"""

"""
def verifyMatrix(matrix):
    height = len(matrix)
    badRows = {}

    for i in range(0, height):
        row = matrix[i]
        length = len(row)

        if (length != height):
            badRows[i] = length

    if badRows:
        message = "Matrix needs to be NxN! Found bad rows:\n\tRow\tLength\n"
        for key in badRows.keys():
            message += "\t%d\t%d\n" % (key, badRows[key])
        raise Exception(message)