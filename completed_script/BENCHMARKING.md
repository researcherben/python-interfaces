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

