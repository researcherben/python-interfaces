#!/usr/bin/env python3
import sys      # command-line arguments
import random   # for graph construction; https://docs.python.org/3/library/random.html

# docstrings should conform to
# https://google.github.io/styleguide/pyguide.html

"""
this file can be used to
 * create a file of edges on disk
 * write edge list to stdout
 * provide the edge list of a graph using a generator
 * provide the graph as a data structure using a function call
See associated README.md for examples

this file is also intended as an examplar for how to use
* logging
* argparse
"""


def create_random_graph(number_of_nodes: int) -> dict:
    """ generate a graph based on user input and return a dictionary

    data structure of interest

    Args:
        number_of_nodes: how many nodes in the graph

    Returns:
        the_graph: a dictionary where each key is a non-negative integer and
        the value is a list of integers corresponding to nearest-neighbor nodes

        {'0': [],
         '2': [1, 3],
         '1': [2],
         '3': [2]}

    >>> create_random_graph(4) #doctest:+SKIP
    {0: [], 1: [2], 2: [1, 3], 3: [2]}
    """
    the_graph = {}

    for node_id in range(number_of_nodes):
        # https://note.nkmk.me/en/python-random-choice-sample-choices/
        edge_list = random.sample(range(number_of_nodes),
                                           random.choice(range(number_of_nodes)))
        if node_id in edge_list:
            edge_list.remove(node_id)
        the_graph[node_id] = edge_list
    return the_graph


if __name__ == "__main__":
    the_graph = create_random_graph(sys.argv[1])
    print(the_graph)
