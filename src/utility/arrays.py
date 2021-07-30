"""
    Utility functionality regarding arrays.

    @author:  Zimon Kuhs.
    @date:    2021-07-12.
"""

"""
    Checks whether or not an object is a jagged matrix.

    @param matrix  The object to check.
    @return        True if the input is not an NxN-matrix.
"""
def isJagged(matrix):
    if not isMatrix(matrix):
        return False

    size = len(matrix)
    for x in range(0, size):
        if (len(matrix[x]) != size):
            return True

    return False

"""
    Checks whether or not an object is a matrix.

    @param matrix  The object to check.
    @return        True if the input is an array of arrays.
"""
def isMatrix(matrix):
    if not isinstance(matrix, list):
        return False

    if len(matrix) == 0:
        return False

    return isinstance(matrix[0], list)
