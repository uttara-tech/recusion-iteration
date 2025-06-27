"""
This module has a simple implementation of Floyd's Algorithm
It contains three main functions:
    main -> controls the execution of the script
    print_out_graph -> prints out the graph with nodes and distances
    recursive_floyd_warshall -> computes shortest path

The global variables are:
    NO_PATH = Marker for where there is no path. This is the max value of an integer
    GRAPH = Contains the distances for the graph. Node names are inferred by the position
    of the node, i.e. position  0 0 in the list is node 0
    MAX_LENGTH = The size of the graph
    MIN_LEVEL = The lowest search level for the shortest path calculation
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function. 
"""
from sys import maxsize
NO_PATH =  maxsize
GRAPH = [[0,   7,  NO_PATH, 8],
[NO_PATH,  0,  5,  NO_PATH],
[NO_PATH, NO_PATH, 0,   2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(GRAPH[0])
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"

def main():
    """
    This is the calling function for the recursive floyd's algorithm
    """
    # function call to recursive_floyd_warshall
    recursive_floyd_warshall(MAX_LENGTH-1, MAX_LENGTH-1, MAX_LENGTH-1)

    #print resulting matrix with the shortest path values
    print_out_graph()

def print_out_graph():
    """
    This function prints out the graph with the distances
    and a place holder for no path between nodes
    """
    for start_node in range(0,MAX_LENGTH):
        for end_node in range(0,MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER 

            message = "Distance from Node %s to Node %s is %s" %\
                (start_node,end_node,distance)
            print (message)



def recursive_floyd_warshall(outer_loop:int, middle_loop:int, inner_loop:int):
        """
        This function computes shortest path between each pair of nodes
        It computes by comparing a direct path
        with paths that have intermediate nodes in the path.

        The recursive path is the shortest path function which
        calls itself to find the shortest path between a pair of nodes

        param: outer_loop: represents the source node
        param: middle_loop: represents the intermediate node
        param: inner_loop: represents the destination node
        """

        # Floyd Warshall algorithmic formula
        GRAPH[outer_loop][inner_loop] = min(GRAPH[outer_loop][inner_loop],
                                          GRAPH[outer_loop][middle_loop] + GRAPH[middle_loop][inner_loop])

        if  inner_loop == MIN_LEVEL and inner_loop != outer_loop:
            inner_loop = MAX_LENGTH -1
            outer_loop -= 1
        elif outer_loop == inner_loop == MIN_LEVEL and middle_loop != MIN_LEVEL:
            inner_loop = MAX_LENGTH -1
            outer_loop = MAX_LENGTH - 1
            middle_loop -= 1
        elif outer_loop == middle_loop == inner_loop == MIN_LEVEL:
            # Exit recursive loop
            return GRAPH
        else:
            inner_loop -= 1

        return recursive_floyd_warshall(outer_loop, middle_loop, inner_loop)
                

def recursive_performance_test():
    """
    This is a procedure call just for the performance test
    """
    recursive_floyd_warshall(MAX_LENGTH - 1, MAX_LENGTH - 1, MAX_LENGTH - 1)


if __name__ == "__main__":
    main()







