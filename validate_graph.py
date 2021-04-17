#!/usr/bin/env python3
"""
either
* read edge tuples from stdin
     python3 produce_output.py 4 | python3 validate_graph.py --stdin
or
* read JSON from disk
     python3 validate_graph.py --JSONfilename file.json
or
* generate graph using imported function
     python3 validate_graph.py --numNodes 4

what about a graph can be checked?
* least number of edges per node
* max number of edges per node
* distribution of edges per node
* number of components in the graph

visualization of graph using graphviz
* what if the graph is big? sampling
"""
import sys
import json
import networkx as nx  # https://networkx.org/documentation/stable//reference/introduction.html
import matplotlib.pyplot as plt
import argparse  # https://docs.python.org/3.3/library/argparse.html

# https://realpython.com/command-line-interfaces-python-argparse/

import produce_output
import validate_json_schema


if __name__ == "__main__":

    theparser = argparse.ArgumentParser(
        description="validate graph", allow_abbrev=False
    )

    # https://stackoverflow.com/a/11155124/1164295
    group = theparser.add_mutually_exclusive_group(required=True)
    # it is possible to constrain the input to a range; see https://stackoverflow.com/a/25295717/1164295
    group.add_argument(
        "--numNodes",
        metavar="nodes_in_graph",
        type=int,
        default=-1,
        help="generate graph using Python API. User provides an integer number of nodes.",
    )
    group.add_argument("--JSONfilename", type=str, help="filename of JSON to parse")
    # https://stackoverflow.com/a/15008806/1164295
    group.add_argument(
        "--stdin",
        action="store_true",
        default=False,
        help="read edge tuples from stdin",
    )

    args = theparser.parse_args()

    if args.stdin:
        graph = {}
        for line in sys.stdin:
            # print(line)
            line_as_list = line.strip().replace("(", "").replace(")", "").split(", ")
            # print(line_as_list)
            try:
                graph[int(line_as_list[0])].append(int(line_as_list[1]))
            except KeyError:
                graph[int(line_as_list[0])] = [int(line_as_list[1])]
    elif args.numNodes != -1:
        graph = produce_output.create_random_graph(args.numNodes)
    elif args.JSONfilename:
        with open(args.JSONfilename) as json_file:
            graph = json.load(json_file)
        graph = {int(k): v for k, v in graph.items()}

    # print(graph)
    G = nx.Graph()
    for key, list_of_nodes in graph.items():
        G.add_edges_from([(key, x) for x in list_of_nodes])

    if not nx.is_connected(G):
        raise Exception("graph is not connected")

    # https://stackoverflow.com/a/47451934/1164295
    dict_of_node_and_degree = {}
    for node, val in G.degree():
        dict_of_node_and_degree[node] = val

    print("key=node ID; value = degree")
    print(dict_of_node_and_degree)

    for degree in set(dict_of_node_and_degree.values()):
        print(
            sum(x == degree for x in dict_of_node_and_degree.values()),
            "nodes have degree",
            degree,
        )

    nx.draw(G)  # default spring_layout
    plt.savefig("output.png")
