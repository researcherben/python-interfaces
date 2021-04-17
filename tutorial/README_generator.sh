#!/usr/bin/env bash

readme_filename=README.md

rm ${readme_filename}

cat << endofsnippet > ${readme_filename}
# step 00

The essential aspect of the script: create a dictionary that represents nodes and edges

endofsnippet
cat step00_produce_output.py | sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

# step 01

Convert the script to something that can be run in the command line or used as library

Add type hints for mypy

endofsnippet
diff -baur step00_produce_output.py step01_produce_output.py |\
       tail -n +4 |\
       sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

# step 02

Added module docstring and docstring for function.
As a consequence, help(create_random_graph) is available

# step 03

Created helper function that uses generator as an alternative mechanism for getting the result

endofsnippet
diff -buar \
     -U$(wc -l step03_produce_output.py | tr -s ' ' | cut -d' ' -f2) step02_produce_output.py step03_produce_output.py |\
       tail -n +4 |\
       sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

# step 04

Use argparse instead of sys.argv

endofsnippet
diff -buar \
     -U$(wc -l step04_produce_output.py | tr -s ' ' | cut -d' ' -f2) step03_produce_output.py step04_produce_output.py |\
       tail -n +4 |\
       sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

# step 05

Add logging

endofsnippet
diff -buar \
     -U$(wc -l step05_produce_output.py | tr -s ' ' | cut -d' ' -f2) step04_produce_output.py step05_produce_output.py |\
       tail -n +4 |\
       sed -e 's/^/    /g' >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}
