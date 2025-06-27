from sys import maxsize

NO_PATH =  maxsize

"""
  The variable 'expectedResult_1' defines an expected output, 
  corresponding to the input global variable GRAPH in recursive_floyd.py file.
  The test case is designed this way to align with the given code framework 
  for recursive_floyd_warshall function.
 """

expectedResult_1 = [[0, 7, 12, 8],
 [NO_PATH, 0, 5, 7],
 [NO_PATH, NO_PATH, 0, 2],
 [NO_PATH, NO_PATH, NO_PATH, 0]
]

"""
 This test_plan.py file can be improved further by:
   a) adding a input test case matrix along-with the expected_result. 
     e.g. testCase_1 = [
                        [0,   7,  NO_PATH, 8],
                        [NO_PATH,  0,  5,  NO_PATH],
                        [NO_PATH, NO_PATH, 0,   2],
                        [NO_PATH, NO_PATH, NO_PATH, 0]
                       ]
                       
     expectedResult_1 = [
                        [0, 7, 12, 8],
                        [NO_PATH, 0, 5, 7],
                        [NO_PATH, NO_PATH, 0, 2],
                        [NO_PATH, NO_PATH, NO_PATH, 0]
                       ]
     testCase_<n> = [...]
     expectedResult_<n> = [...]
  
  b) by using nested functions and passing an entire matrix (e.g. GRAPH) as an argument 
  to the recursive_floyd_warshall function. 
  
  With a) and b), we can define and test multiple test cases here (triggered from unittests.py file).

"""
