What would it take to get a simple Python script to be production quality?

Given a trivial task (e.g., generate a random graph), implement all the best practices.

Here's the "trivial task" -- 12 lines of Python 3. 
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
* wrap the code snippet in a function and then have `main` call the function allows other developers to use that same capability elsewhere by importing the function. See `tutorial_on_how_to_evolve_from_research-grade_to_production/input_files/step01_produce_output.py`
* document the function with a comment block that enables `help`. See `tutorial_on_how_to_evolve_from_research-grade_to_production/input_files/step02_produce_output.py`
* provide command-line help when calling the .py file
* implement logging capability
* wrapping the snippet in a function implies testing the function
* fuzz testing
  * <https://www.fuzzingbook.org/html/Fuzzer.html>
  * <https://fuzzing.readthedocs.io/en/latest/tutorial.html>
  * <https://github.com/google/atheris> and <https://opensource.googleblog.com/2020/12/announcing-atheris-python-fuzzer.html>
* behavioral tests
* regression tests
* performance characterization: scaling tests of memory, wall-clock time
* does the code enact the required capability? 
* create sphinx documentation
* containerize dependencies
* specify version for python dependencies. Better: specify hash for Python dependencies. See <https://github.com/pypa/packaging.python.org/issues/564#issuecomment-428011603> and <https://lil.law.harvard.edu/blog/2019/05/20/improving-pip-compile-generate-hashes/>
* cache the python dependencies offline (rather than relying on pypi over the network)
* build python dependencies from source (rather than relying on wheels)


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


