"""
@author:  Zimon Kuhs.
@date:    2021-07-12.
"""

import unittest

import utility.arrays as arrays


class TestEuler(unittest.TestCase):
    """
        This test class runs tests of array utilities.
    """

    def __init__self(self):
        pass

    """
        Verifies that the identity method isMatrix(object) behaves correctly for arrays, arrays of arrays,
        and dictionaries.
    """
    def testIsMatrix(self):
        self.assertTrue(arrays.isMatrix([[]]), "Should be true for a 1x0 matrix.")
        self.assertTrue(arrays.isMatrix([[0, 0], [0, 0]]), "Should be true for basic example.")
        self.assertTrue(arrays.isMatrix([[0, 0], [0], [0, 0, 0, 0]]), "Should be true for jagged matrices.")
        self.assertFalse(arrays.isMatrix([]), "Should be false for empty array.")
        self.assertFalse(arrays.isMatrix([0, 0]), "Should be false for arrays.")
        self.assertFalse(arrays.isMatrix({"key1": "value1", "key2": "value2"}), "Should be false for dictionaries.")
        self.assertFalse(arrays.isMatrix({"key1": {"key11": "value11", "key12": "value12"},
                                          "key2": {"key21": "value21", "key22": "value22"}}),
                                          "Should be false for dictionaries containing dictionaries.")

    """
        Verifies that the identity method isJagged(object) correctly identifies arrays, arrays of arrays,
        and dictionaries, as being or not being jagged matrices.
    """
    def testIsJagged(self):
        self.assertTrue(arrays.isJagged([[0, 0], [0], [0, 0, 0, 0]]), "Should be true for jagged matrices.")
        self.assertTrue(arrays.isJagged([[]]), "Should be true for a 1x0 matrix.")
        self.assertFalse(arrays.isJagged([]), "Should be false for empty array.")
        self.assertFalse(arrays.isJagged([[0, 0], [0, 0]]), "Should be false for basic example.")
        self.assertFalse(arrays.isJagged([0, 0]), "Should be false for arrays.")
        self.assertFalse(arrays.isJagged({"key1": "value1", "key2": "value2"}), "Should be false for dictionaries.")
        self.assertFalse(arrays.isJagged({"key1": {"key11": "value11", "key12": "value12"},
                                          "key2": {"key21": "value21", "key22": "value22"}}),
                                          "Should be false for dictionaries containing dictionaries.")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
