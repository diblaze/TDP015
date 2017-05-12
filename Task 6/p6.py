# TDP015 Programming Assignment 6
import json
import time
from pprint import pprint


# In one of my current research projects, I am developing algorithms
# for the parsing of natural language to meaning representations in
# the form of directed graphs:
#
# http://www.ida.liu.se/~marku61/ceniit.shtml
#
# A desirable property of these graphs is that they should be acyclic,
# that is, should not contain any (directed) cycles. Your task in this
# assignment is to implement a Python function that tests this
# property, and to apply your function to compute the number of cyclic
# graphs in one of the datasets that I am using in my research.
#
# Your final script should be callable from the command line as follows:
#
# python3 p6.py ccg.train.json
#
# This should print out the IDs of the cyclic graphs in the specified
# file, in the same order in which these graph appear in the file:
#
# $ python3 p6.py foo.json
# 22172056
# 22153010
# 22106047
#
# The graphs are stored in a JSON file containing a single dictionary
# mapping graph ids (8-digit integers starting with 22) to graphs, where
# each graph is represented as a dictionary mapping vertices (or rather
# their ids) to lists of neighbouring vertices.


# RECURSIVE
def cyclic(graph):
    """Test whether the directed graph `graph` has a (directed) cycle.

    The input graph needs to be represented as a dictionary mapping vertex
    ids to iterables of ids of neighboring vertices. Example:

    {"1": ["2"], "2": ["3"], "3": ["1"]}

    Args:
        graph: A directed graph.

    Returns:
        `True` if the directed graph `graph` has a (directed) cycle.
    """

    # Idea to color nodes as visited gotten from:
    # http://stackoverflow.com/questions/28913762/vertex-coloring-with-dfs

    # I will be using the depth-first search algorithm.
    # Which works by initializing two dictionaries, one that holds visited nodes,
    # and the second one that holds colors for specific nodes (i.e the graph).
    # We start by visting all nodes, and when we visit a node, we color it 'grey' -
    # this indicates the node is part of the current path.
    # We then visit the neighbors of that node (neighbors should be 'white', i.e not visited),
    # if we visit a node that is 'grey' then we have a cycle.
    # When we are done with all neighbors of the current node, we color it 'black'
    # indicating that we are moving on to a second node.

    # init the dict
    color = {}
    # apperntly Python doesn't pass reference as other langauges... but it can
    # pass Objects perfectly (value by reference)
    cycle  = [False]

    # set all nodes to unvisisted
    for node in graph:
        color[node] = "non-visited"

    def visit(node, graph, cycle, color):  # don't hate me for doing a function inside of a function :D
        color[node] = "visited"  # set current node to visited
        for neighbor in graph[node]:  # check all neighbors to the current node
            if color[neighbor] == "visited":  # have we visited it already?
                cycle[0] = True  # cycle found
                return  # jump out of function because we found a cyclic graph
            elif color[neighbor] == "non-visited":  # if we havent visited the neighbor
                # visit it and check its neighbors
                visit(neighbor, graph, cycle, color)
        # mark node as black, to indicate that we have been here, but we can
        # still run the search.
        color[node] = "again"

    for node in graph:  # go through each node in the given graph
        if color[node] == "non-visited":  # if not visited
            visit(node, graph, cycle, color)  # visit

    return cycle[0]  # no cycle found, return false


if __name__ == "__main__":
    graph_example_true1 = {'0': ['1'],
                           '1': ['2'],
                           '2': ['3'],
                           '3': ['4'],
                           '4': ['1']}
    graph_example_false1 = {'0': ['1', '2'],
                            '1': ['2'],
                            '2': []}
    graph_example_true2 = {'0': ['1', '2'],
                           '1': [],
                           '2': ['3'],
                           '3': ['4'],
                           '4': ['2']}
    graph_example_false2 = {'0': [],
                            '1': [],
                            '2': [],
                            '3': []}

    #Test cases to make sure it is working  - START    
    #print(cyclic(graph_example_true1))
    assert(cyclic(graph_example_true1) == True)

    #print(cyclic(graph_example_false1))
    assert(cyclic(graph_example_false1) == False)

    #print(cyclic(graph_example_true2))
    assert(cyclic(graph_example_true2) == True)

    #print(cyclic(graph_example_false2))
    assert(cyclic(graph_example_false2) == False)
    #Test cases to make sure it is working  - END  

    graph_data = {}
    #read all json into one big dict
    with open('./ccg.train.json') as data:
        graph_data = json.load(data)

    ids = []
    start = time.time()
    #go through each graph
    for graph in graph_data:
        #check if it is cyclic
        g = graph_data[graph] 
        if cyclic(g): #couldnt send graph_data directly to cyclic for some reason, got error, thats why I assign to 'g'.
            #if cyclic, then append the id to the list.
            ids.append(graph)
        else:
            continue
    end = time.time()
    
    #print each ID as the task said
    for id in ids:
        pprint(id)
    
    print("The search algorithm took: " + str(end-start) + " seconds to complete.") #average ~= 0.36s
    print(str(len(graph_data)) + " number of graphs.")
    print(str(len(ids)) + " number of cyclic graphs")
