# TDP015 Programming Assignment 6

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
    # TODO: Replace the following line with your own code.

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
    cycle = False
    for node in graph:
        color[node] = "white"

    def visit(node, graph, cycle, color):
        if cycle == True:
            return cycle
        color[node] = "grey"
        for neighbor in graph[node]:
            if color[neighbor] == "grey":
                cycle = True
                return cycle
            if color[neighbor] == "white":
                return visit(neighbor, graph, cycle, color)
        color[node] = "black"

    for node in graph:
        if color[node] == "white":
            cycle = visit(node, graph, cycle, color)
        if cycle:
            return cycle

    if cycle == None:  # not really sure why it returns None... Can't find the issue
        cycle = False
    return cycle


if __name__ == "__main__":
    graph_example_true1 = {0: [1],
                           1: [2],
                           2: [3],
                           3: [4],
                           4: [1]}
    graph_example_false1 = {0: [1, 2],
                            1: [2],
                            2: []}
    graph_example_true2 = {0: [1, 2],
                           1: [],
                           2: [3],
                           3: [4],
                           4: [2]}
    graph_example_false2 = {0: [],
                            1: [],
                            2: [],
                            3: []}

    print(cyclic(graph_example_true1))
    assert(cyclic(graph_example_true1) == True)

    print(cyclic(graph_example_false1))
    assert(cyclic(graph_example_false1) == False)

    print(cyclic(graph_example_true2))
    assert(cyclic(graph_example_true2) == True)

    print(cyclic(graph_example_false2))
    assert(cyclic(graph_example_false2) == False)
