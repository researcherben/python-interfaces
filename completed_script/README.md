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
