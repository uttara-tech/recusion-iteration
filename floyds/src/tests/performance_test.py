"""
This module contains a simple performance test which
compares the recursive version of Floyd's algorithm with the
iterative version
"""

import sys
import timeit

sys.path.append('../')
from src.recursion.recursive_floyd import recursive_performance_test
from src.iterative.iterative_floyd import iterative_floyd


def performance_test(function_handle):
    """
    Performance test for Floyd's algorithm - Iterative Vs Recursive
    """
    return timeit.timeit(function_handle, number=1)
    

# Calculate time in second(s) for recursive function
duration = performance_test(recursive_performance_test)
print ("Recursion Test Time", duration)

# Calculate time in second(s) for iterative function
duration = performance_test(iterative_floyd)
print ("Iterative Test Time", duration)









    


