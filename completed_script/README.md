in addition to the Python cleanliness tools in the Makefile, there are two additional test script written specifically to evaluate `produce_output.py`

```bash
docker run -it -v `pwd`:/scratch --rm interface_demo /bin/sh -c "python3 produce_output.py 4 | python3 validate_graph.py --stdin"
    key=node ID; value = degree
    {0: 3, 2: 2, 1: 3, 3: 2}
    2 nodes have degree 2
    2 nodes have degree 3
```



```bash
docker run -it -v `pwd`:/scratch --rm interface_demo python3 produce_output.py 4 --json > my_output.json

docker run -it -v `pwd`:/scratch --rm interface_demo python3 validate_json_schema.py /scratch/my_output.json 
    Successfully validated file against schema
```


# doctest

```bash
make doctest
    python3 -m doctest -v produce_output.py
    3 items had no tests:
        produce_output
        produce_output.create_random_graph
        produce_output.next_edge_in_graph
    0 tests in 3 items.
    0 passed and 0 failed.
    Test passed.
```

# mypy

```bash
make mypy
    mypy --check-untyped-defs produce_output.py
    Success: no issues found in 1 source file
```

# black

```bash
make black
    black produce_output.py
    All done! ✨ 🍰 ✨
    1 file left unchanged.
```

# mccabe

```bash
make mccabe
python3 -m mccabe produce_output.py
If 43 2
108:0: 'create_random_graph' 3
153:0: 'next_edge_in_graph' 3
If 176 7
```

EOF