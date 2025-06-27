"""
This module defines two test cases for unit testing.
More test cases can be added here for a sequential execution.
Define corresponding output variables in test_plan.py file.
To define more testcases, please refer the __doc__ string of the test_plan file.
"""

import sys
sys.path.append('../')
import unittest
import test_plan
from src.recursion.recursive_floyd import *

class TestRecursiveFloyd(unittest.TestCase):
    def test_floyd(self):
        """
        Test case to check the output of recursive_floyd_warshall function.
        It should match with the expected output.
        """
        max_size = len(GRAPH)
        self.assertEqual(recursive_floyd_warshall(max_size - 1, max_size - 1, max_size - 1), test_plan.expectedResult_1)

    def test_floyd_2(self):
        """
        Test case to check an incorrect input.
        It should not match with the expected output.
        """
        max_size = len(GRAPH)
        self.assertIsNot(recursive_floyd_warshall(max_size - 3, max_size - 3, max_size - 3), test_plan.expectedResult_1)

if __name__ == '__main__':
    unittest.main()

