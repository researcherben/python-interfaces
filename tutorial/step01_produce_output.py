#!/usr/bin/env python3
import sys  # command-line arguments
# https://docs.python.org/3/library/random.html
import random  # for graph construction


def create_random_graph(number_of_nodes: int) -> dict:
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


if __name__ == "__main__":
    number_of_nodes = int(sys.argv[1])
    the_graph = create_random_graph(number_of_nodes)
    print(the_graph)
