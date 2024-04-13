What would it take to get a simple Python script to be production quality?

Given a trivial task (here we generate a random graph), implement all the best practices.

```python
#!/usr/bin/env python3
import sys  # command-line arguments
import random  # for graph construction
number_of_nodes = int(sys.argv[1])
the_graph = {}
for node_id in range(number_of_nodes):
    edge_list = random.sample(
        range(number_of_nodes), random.choice(range(number_of_nodes)))
    if node_id in edge_list:
        edge_list.remove(node_id)
    the_graph[node_id] = edge_list
print(the_graph)
````

For example, 
* wrap the code snippet in a function and then having `main` call the function allows other developers to use that same capability elsewhere by importing the function. See `tutorial_on_how_to_evolve_from_research-grade_to_production/input_files/step01_produce_output.py`
* document the function with a comment block that enables `help`. See `tutorial_on_how_to_evolve_from_research-grade_to_production/input_files/step02_produce_output.py`
* provide command-line help when calling the .py file
* implement logging capability 
* wrap the snippet in a function implies testing the function
* fuzz testing
* regression testing
* performance characterization: scaling tests of memory, wall-clock time
* does the code enact the required capability? 
* create sphinx documentation

There are 4 ways to explore this project:
* look in the folder `completed_script` for the result.
* The tutorial folder contains the progression of adding the capabilities to the trivial task.
  * as a sequence of `.py` files; see `tutorial_on_how_to_evolve_from_research-grade_to_production/input_files/`
  * as a README containing the progression as in-line diffs: `tutorial_on_how_to_evolve_from_research-grade_to_production/README_inline_diff.md`
  * as a README containing the progression as side-by-side diffs: `tutorial_on_how_to_evolve_from_research-grade_to_production/README_diff_side-by-side.md`


### TODO: 

- [ ] write a set of formal requirements against which to evaluate the implementation
- [ ] test for structural consistency against defined specifications.
- [ ] Validate that the Python functions are consistent with API definition
   - [ ] no extra return values
   - [ ] data type correct
   - [ ] correct types in keys and values
   - [ ] valid ranges per variable (int >= 0)


# what happens if no arguments are provided?

Here we assume all necessary packages are on the host

```bash
python3 completed_script/produce_output.py
    usage: produce_output.py [-h] nodes_in_graph
    produce_output.py: error: the following arguments are required: nodes_in_graph
```

If you have compiled the Docker image, then

```bash
docker run -it -v `pwd`:/scratch --rm interface_demo python3 /scratch/completed_script/produce_output.py
    usage: produce_output.py [-h] nodes_in_graph
    produce_output.py: error: the following arguments are required: nodes_in_graph
```

For the rest of these examples you can prefix the command with `docker run -it -v `pwd`:/scratch --rm interface_demo /scratch` as needed.

# run as script

```
python3 produce_output.py 4
    (3, 0)
    (3, 2)
    (3, 1)
```

# help message

```bash
python3 produce_output.py --help
    usage: produce_output.py [-h] nodes_in_graph

    generate a graph

    positional arguments:
      nodes_in_graph  an integer number of nodes

    optional arguments:
      -h, --help      show this help message and exit
      --seed random_seed  random seed used by Python
```
# write to file on disk

    python3 produce_output.py 4 > file.dat

# write to stdout

    python3 produce_output.py 4 | grep 3
    (3, 2)
    (3, 3)
    (3, 0)

# interactive help

    python3
    >>> import produce_output
    >>> help(produce_output.create_random_graph)

    Help on function create_random_graph in module produce_output:
    create_random_graph(number_of_nodes: int) -> dict
       generate a graph based on user input and return a dictionary
       primary data structure of interest
       Args:
           number_of_nodes: how many nodes in the graph
       Returns:
           the_graph: a dictionary where each key is a non-negative integer and
           the value is a list of integers corresponding to nearest-neighbor nodes
           {'2': [1, 3],
            '1': [2],
            '3': [2]}

       >>> create_random_graph(4)


# use as a library, return full dictionary

    python3
    >>> import produce_output
    >>> produce_output.create_random_graph(4)
    {0: [], 1: [3, 1], 2: [], 3: [2, 3]}

# use as a library, return generator

    python3
    >>> import produce_output
    >>> for edge_tuple in produce_output.next_edge_from_graph_of_size(4):
    ...     print(edge_tuple)
    ...
    (0, 1)
    (1, 0)
    (1, 2)
    (1, 3)
    (2, 2)
    (3, 2)


# benchmarking
logging is enabled during all of these benchmarks
## STDOUT
not expected to scale well
### write to file; random graph

    for ((i = 0 ; i <= 3000 ; i=i+500)); do echo i=$i; rm file; time python3 produce_output.py $i > file; ls -hal file; done
    i=0    | 0m 0.183s |  0B
    i=500  | 0m 0.663s |  1.2M
    i=1000 | 0m 2.242s |  5.2M
    i=1500 | 0m 4.786s | 12M
    i=2000 | 0m 7.957s | 23M
    i=2500 | 0m12.867s | 36M
    i=3000 | 0m17.987s | 52M

### write to /dev/null; random graph

Same timing as writing to file

    for ((i = 0 ; i <= 3000 ; i=i+500)); do echo i=$i; time python3 produce_output.py $i > /dev/null; done
    i=0    | 0m0.176s
    i=500  | 0m0.634s
    i=1000 | 0m2.061s
    i=1500 | 0m5.023s
    i=2000 | 0m9.893s
    i=2500 | 0m14.242s
    i=3000 | 0m18.284s

## create data structure
Python API, expected to scale
### create data structure; random graph

For the same size graph writing to STDOUT, creating the data structure is much faster.
That shows how much cost STDOUT has on execution duration.

    for ((i = 0 ; i <= 3000 ; i=i+500)); do echo i=$i; python3 -m timeit -n 1 --repeat=1 --unit=sec --verbose "import produce_output; produce_output.create_random_graph(${i})"; done
    i=0    | 0.118 sec
    i=500  | 0.282 sec
    i=1000 | 0.842 sec
    i=1500 | 1.88 sec
    i=2000 | 3.05 sec
    i=2500 | 5.03 sec
    i=3000 | 7.38 sec

### create data structure; fully connected graph

For the same size graph as the random graph, "fully connected" is much faster.
That shows that the "import random" is the cause of the slow-down.

    for ((i = 0 ; i <= 3000 ; i=i+500)); do echo i=$i; python3 -m timeit -n 1 --repeat=1 --unit=sec --verbose "import produce_output; produce_output.create_fully_connected_graph(${i})"; done
    i=0    | 0.0832 sec
    i=500  | 0.0926 sec
    i=1000 | 0.149 sec
    i=1500 | 0.232 sec
    i=2000 | 0.356 sec
    i=2500 | 0.522 sec
    i=3000 | 0.728 sec

As graph size increases, memory allocation for the graph becomes the bottleneck

    for ((i = 1000 ; i <= 10000 ; i=i+1000)); do echo i=$i; python3 -m timeit -n 1 --repeat=1 --unit=sec --verbose "import produce_output; produce_output.create_fully_connected_graph(${i})"; done
    i=1000  |  0.144 sec
    i=2000  |  0.368 sec
    i=3000  |  0.734 sec
    i=4000  |  1.33 sec
    i=5000  |  2.36 sec
    i=6000  |  3.55 sec
    i=7000  |  5.06 sec
    i=8000  |  7 sec
    i=9000  | 10.2 sec
    i=10000 | 13.1 sec

### create data structure; ring graph

A ring graph is memory efficient and easy to generate

    python3 -c "import produce_output; print(produce_output.create_ring_graph(4))"
    {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 0}

I didn't find a bottleneck!

    for ((i = 1000000000000000 ; i <= 10000000000000000 ; i=i+2000000000000000)); do echo i=$i; python3 -m timeit -n 1 --repeat=1 --unit=sec --verbose "import produce_output; produce_output.create_ring_graph(${i})"; done
    i=1000000000000000 | 0.0862 sec
    i=3000000000000000 | 0.0848 sec
    i=5000000000000000 | 0.0833 sec
    i=7000000000000000 | 0.0851 sec
    i=9000000000000000 | 0.0832 sec
