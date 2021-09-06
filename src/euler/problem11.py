"""
    'Largest Product in a Grid'

    https://projecteuler.net/problem=11

    @author:    Zimon Kuhs.
    @date:      2021-07-09.
    @solution:  70600674
"""

import sys

import utility.arrays as arrays

"""
    Finds the largest product of a specified amount matrix elements, either column-wise, row-wise, or diagonally.

    @param matrix   The matrix in which to find the largest product.
    @param reach    The amount of elements to use when calculating products.
    @return         The largest product of a set of numbers, within a specified reach in either uniform matrix direction.
"""
def solve(matrix, reach):
    if arrays.isJagged(matrix):
        raiseJaggedError(matrix)

    biggest = -sys.maxsize - 1
    dimension = len(matrix)

    for i in range(0, dimension - reach):
        for j in range(0, dimension - reach):
            products = [1, 1, 1, 1]

            for x in range(0, reach):
                products[0] *= matrix[i + x][j]
                products[1] *= matrix[i][j + x]
                products[2] *= matrix[i + x][j + x]
                products[3] *= matrix[i - x][j + x]

            biggest = max(biggest, max(products))

    return biggest

"""
    Checks that the input matrix is a two-dimensional array.
    Each *row* which length does not equal the column length (amount of rows) is reported as erroneous.

    @param matrix    The matrix to check.
    @raise Exception If the input matrix is jagged.
"""
def raiseJaggedError(matrix):
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
