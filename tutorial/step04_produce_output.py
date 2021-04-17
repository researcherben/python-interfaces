#!/usr/bin/env python3
import random  # for graph construction; https://docs.python.org/3/library/random.html
import argparse  # https://docs.python.org/3.3/library/argparse.html

# https://realpython.com/command-line-interfaces-python-argparse/

# import sys
# I had been using sys for command-line arguments as per
#       https://realpython.com/python-command-line-arguments/
#       but argparse is the better approach
# I had intended to use sys for for writing to stderr as per
#       https://stackoverflow.com/a/15808105/1164295
#       but logging is the better approach


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
    """generate a graph based on user input and return a dictionary

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
    logger.info("[trace]")
    the_graph = {}

    for node_id in range(number_of_nodes):
        # https://note.nkmk.me/en/python-random-choice-sample-choices/
        edge_list = random.sample(
            range(number_of_nodes), random.choice(range(number_of_nodes))
        )
        if node_id in edge_list:
            edge_list.remove(node_id)
        the_graph[node_id] = edge_list
    return the_graph


# ********** begin helper functions *****************


def next_edge_in_graph(the_graph: dict):
    """generate every edge in the_graph

    generator of edges
    This is a helper function to access the primary data structure

    Args:
        the_graph: a dictionary where each key is a non-negative integer and
        the value is a list of integers corresponding to nearest-neighbor nodes

    Returns:
        tuple of 2 integers. Each integer is the index of a node

    >>> next_edge_in_graph({}) #doctest:+SKIP
    """
    for left_node, list_of_nodes in the_graph.items():
        for right_node in list_of_nodes:
            yield ((left_node, right_node))


def next_edge_from_graph_of_size(num_nodes: int):
    """generate every edge in a graph of size num_nodes

    generator of edges
    This is a helper function to access the primary data structure

    Args:
        num_nodes: number of nodes in graph

    Returns:
        tuple of 2 integers. Each integer is the index of a node

    >>> next_edge_from_graph_of_size(4) #doctest:+SKIP
    """
    the_graph = create_graph(num_nodes)

    for edge_tuple in next_edge_in_graph(the_graph):
        yield (edge_tuple)


# ********** end helper functions *****************

if __name__ == "__main__":
    # testing sys.argv isn't needed since argparse is being used
    #    if len(sys.argv)<2: # no command-line arguments
    # print to stdout to enable file-on-disk or piped workflow
    #        print("fatal error", file=sys.stderr)

    # ********** begin argparse configuration *****************

    theparser = argparse.ArgumentParser(
        description="generate a graph", allow_abbrev=False
    )

    # required positional argument
    # it is possible to constrain the input to a range; see https://stackoverflow.com/a/25295717/1164295
    theparser.add_argument(
        "numNodes",
        metavar="nodes_in_graph",
        type=int,
        default=5,
        help="an integer number of nodes",
    )
    # optional argument
    # setting random_seed is useful for consistency when testing
    # max value of seed is discussed on https://stackoverflow.com/a/50808998/1164295
    theparser.add_argument(
        "--seed",
        metavar="random_seed",
        type=int,
        default=None,
        help="random seed used by Python",
    )

    # ********** end argparse configuration *****************

    args = theparser.parse_args()

    random.seed(args.seed)

    the_graph = create_random_graph(args.numNodes)

    for edge_tuple in next_edge_in_graph(the_graph):
        print(edge_tuple)
