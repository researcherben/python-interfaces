#!/usr/bin/env python3
# https://docs.python.org/3/library/random.html
import random  # for graph construction
import logging  # https://docs.python.org/3/library/logging.html

# https://realpython.com/python-logging-source-code/
import argparse  # https://docs.python.org/3.3/library/argparse.html

# https://realpython.com/command-line-interfaces-python-argparse/
import os

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

this file is also intended as an exemplar for how to use
* logging
* argparse
"""


# ************ Begin logging configuration ******************
# logging should be configured once (not per module)
# other modules can then reference the configuration


if not os.path.exists("logs"):
    os.makedirs("logs")

# https://gist.github.com/ibeex/3257877
from logging.handlers import RotatingFileHandler

# maxBytes=10000 = 10kB
# maxBytes=100000 = 100kB
# maxBytes=1000000 = 1MB
# maxBytes=10000000 = 10MB
log_size = 10000000
# maxBytes=100000000 = 100MB
# https://gist.github.com/ibeex/3257877
handler_debug = RotatingFileHandler(
    "logs/critical_and_error_and_warning_and_info_and_debug.log",
    maxBytes=log_size,
    backupCount=2,
)
handler_debug.setLevel(logging.DEBUG)
handler_info = RotatingFileHandler(
    "logs/critical_and_error_and_warning_and_info.log",
    maxBytes=log_size,
    backupCount=2,
)
handler_info.setLevel(logging.INFO)
handler_warning = RotatingFileHandler(
    "logs/critical_and_error_and_warning.log",
    maxBytes=log_size,
    backupCount=2,
)
handler_warning.setLevel(logging.WARNING)

# https://docs.python.org/3/howto/logging.html
logging.basicConfig(
    # either (filename + filemode) XOR handlers
    # to save entries to file instead of displaying to stderr
    # filename="test.log",
    # https://docs.python.org/dev/library/functions.html#filemodes
    # filemode="w",
    handlers=[handler_debug, handler_info, handler_warning],
    # if the severity level is INFO,
    # the logger will handle only INFO, WARNING, ERROR, and CRITICAL messages
    # and will ignore DEBUG messages
    level=logging.DEBUG,
    format="%(asctime)s|%(filename)-13s|%(levelname)-5s|%(lineno)-4d|%(funcName)-20s|%(message)s"  # ,
    # https://stackoverflow.com/questions/6290739/python-logging-use-milliseconds-in-time-format/7517430#7517430
    # datefmt="%m/%d/%Y %I:%M:%S %f %p",
    # https://strftime.org/
)

# https://docs.python.org/3/howto/logging.html
# if the severity level is INFO, the logger will handle
# only INFO, WARNING, ERROR, and CRITICAL messages and will ignore DEBUG messages
# handler.setLevel(logging.INFO)
# handler.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)

# http://matplotlib.1069221.n5.nabble.com/How-to-turn-off-matplotlib-DEBUG-msgs-td48822.html
# https://github.com/matplotlib/matplotlib/issues/14523
logging.getLogger("matplotlib").setLevel(logging.WARNING)

# ************ end logging configuration ******************

logger = logging.getLogger(__name__)

# ********** begin primary functions *****************


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


# ********** end primary functions *****************

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
    logger.info("[trace]")
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
    logger.info("[trace]")
    the_graph = create_random_graph(num_nodes)

    for edge_tuple in next_edge_in_graph(the_graph):
        yield (edge_tuple)


# ********** end helper functions *****************

if __name__ == "__main__":
    logger.info("[trace]")
    # testing sys.argv isn't needed since argparse is being used
    #    if len(sys.argv)<2: # no command-line arguments
    # print to stdout to enable file-on-disk or piped workflow
    #        print("fatal error", file=sys.stderr)

    # ********** begin argparse configuration *****************

    theparser = argparse.ArgumentParser(
        description="generate a graph", allow_abbrev=False
    )

    # required positional argument
    # it is possible to constrain the input to a range;
    # see https://stackoverflow.com/a/25295717/1164295
    theparser.add_argument(
        "numNodes",
        metavar="nodes_in_graph",
        type=int,
        default=5,
        help="an integer number of nodes",
    )
    # optional argument
    # setting random_seed is useful for consistency when testing
    # max value of seed is discussed on
    # https://stackoverflow.com/a/50808998/1164295
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

    logger.info("user provided " + str(args.numNodes))
    the_graph = create_random_graph(args.numNodes)

    for edge_tuple in next_edge_in_graph(the_graph):
        print(edge_tuple)
