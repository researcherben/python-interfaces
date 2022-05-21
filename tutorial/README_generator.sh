#!/usr/bin/env bash

# https://explainshell.com/explain?cmd=set+-euxo+pipefail
#set -euxo pipefail
set -uxo pipefail
# -e     When this option is on, if a simple command fails for any of the reasons listed in Consequences of
#        Shell  Errors or returns an exit status value >0, and is not part of the compound list following a
#        while, until, or if keyword, and is not a part of an AND  or  OR  list,  and  is  not  a  pipeline
#        preceded by the ! reserved word, then the shell shall immediately exit.
# -u     The shell shall write a message to standard error when it tries to expand a variable that  is  not
#        set and immediately exit. An interactive shell shall not exit.
# -x     The  shell shall write to standard error a trace for each command after it expands the command and
#        before it executes it. It is unspecified whether the command that turns tracing off is traced.
# -o     Write the current settings of the options to standard output in an unspecified format.

readme_filename=README.md

rm -f ${readme_filename}

cat << endofsnippet > ${readme_filename}
# step 00

The essential aspect of the script: create a dictionary that represents nodes and edges

endofsnippet
echo "\`\`\`python" >> ${readme_filename}
#cat step00_produce_output.py | sed -e 's/^/    /g' >> ${readme_filename}
cat step00_produce_output.py >> ${readme_filename}
echo "\`\`\`" >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

The above content is from the file
[step00_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step00_produce_output.py)

# step 01

Convert the script to something that can be run in the command line or used as library

Add type hints for mypy

endofsnippet
echo "\`\`\`python" >> ${readme_filename}
#diff --ignore-space-change \  # ignore changes in the amount of white space
#     --text `# treat all files as text` \
#     --unified=$(wc -l step01_produce_output.py | cut -d' ' -f1) `# output NUM lines of unified context` \
#         step00_produce_output.py step01_produce_output.py |\
#       tail -n +4 >> ${readme_filename}

# https://stackoverflow.com/a/1655488/1164295
max_line_length_1=`awk '{print length, $0}' step00_produce_output.py |sort -nr|head -1|cut -d' ' -f1`
max_line_length_2=`awk '{print length, $0}' step01_produce_output.py |sort -nr|head -1|cut -d' ' -f1`
# https://www.log2base2.com/shell-script-examples/operator/how-to-add-two-variables-in-shell-script.html
total_length=$(($max_line_length_1 + $max_line_length_2))
# https://stackoverflow.com/a/12797512/1164295
diff --ignore-space-change `# ignore changes in the amount of white space` \
     --width=${total_length} \
     --expand-tabs \
     --side-by-side \
        step00_produce_output.py step01_produce_output.py >> ${readme_filename}

echo "\`\`\`" >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

The above content is the diff of
[step00_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step00_produce_output.py)
and
[step01_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step01_produce_output.py)

# step 02

Added module docstring and docstring for function.
As a consequence, \`help(create_random_graph)\` is available

# step 03

Created helper function that uses generator as an alternative mechanism for getting the result

endofsnippet
echo "\`\`\`python" >> ${readme_filename}
# diff --ignore-space-change \  # ignore changes in the amount of white space
#      --text \                 # treat all files as text
#      -U$(wc -l step03_produce_output.py | tr -s ' ' | cut -d' ' -f2) step02_produce_output.py step03_produce_output.py |\
#        tail -n +4 >> ${readme_filename}

# https://stackoverflow.com/a/1655488/1164295
max_line_length_1=`awk '{print length, $0}' step02_produce_output.py |sort -nr|head -1|cut -d' ' -f1`
max_line_length_2=`awk '{print length, $0}' step03_produce_output.py |sort -nr|head -1|cut -d' ' -f1`
# https://www.log2base2.com/shell-script-examples/operator/how-to-add-two-variables-in-shell-script.html
total_length=$(($max_line_length_1 + $max_line_length_2))
# https://stackoverflow.com/a/12797512/1164295
diff --ignore-space-change `# ignore changes in the amount of white space` \
     --width=${total_length} \
     --expand-tabs \
     --side-by-side \
        step02_produce_output.py step03_produce_output.py >> ${readme_filename}


echo "\`\`\`" >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

The above content is the diff of
[step02_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step02_produce_output.py)
and
[step03_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step03_produce_output.py)


# step 04

Use argparse instead of sys.argv

endofsnippet
echo "\`\`\`python" >> ${readme_filename}
# diff --ignore-space-change \  # ignore changes in the amount of white space
#      --text \                 # treat all files as text
#      -U$(wc -l step04_produce_output.py | tr -s ' ' | cut -d' ' -f2) step03_produce_output.py step04_produce_output.py |\
#        tail -n +4 >> ${readme_filename}

# https://stackoverflow.com/a/1655488/1164295
max_line_length_1=`awk '{print length, $0}' step03_produce_output.py |sort -nr|head -1|cut -d' ' -f1`
max_line_length_2=`awk '{print length, $0}' step04_produce_output.py |sort -nr|head -1|cut -d' ' -f1`
# https://www.log2base2.com/shell-script-examples/operator/how-to-add-two-variables-in-shell-script.html
total_length=$(($max_line_length_1 + $max_line_length_2))
# https://stackoverflow.com/a/12797512/1164295
diff --ignore-space-change `# ignore changes in the amount of white space` \
     --width=${total_length} \
     --expand-tabs \
     --side-by-side \
        step03_produce_output.py step04_produce_output.py >> ${readme_filename}

echo "\`\`\`" >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

The above content is the diff of
[step03_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step03_produce_output.py)
and
[step04_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step04_produce_output.py)


# step 05

Add logging

endofsnippet
echo "\`\`\`python" >> ${readme_filename}
# diff -buar \
#      -U$(wc -l step05_produce_output.py | tr -s ' ' | cut -d' ' -f2) step04_produce_output.py step05_produce_output.py |\
#        tail -n +4 >> ${readme_filename}

# https://stackoverflow.com/a/1655488/1164295
max_line_length_1=`awk '{print length, $0}' step04_produce_output.py |sort -nr|head -1|cut -d' ' -f1`
max_line_length_2=`awk '{print length, $0}' step05_produce_output.py |sort -nr|head -1|cut -d' ' -f1`
# https://www.log2base2.com/shell-script-examples/operator/how-to-add-two-variables-in-shell-script.html
total_length=$(($max_line_length_1 + $max_line_length_2))
# https://stackoverflow.com/a/12797512/1164295
diff --ignore-space-change `# ignore changes in the amount of white space` \
     --width=${total_length} \
     --expand-tabs \
     --side-by-side \
        step04_produce_output.py step05_produce_output.py >> ${readme_filename}


echo "\`\`\`" >> ${readme_filename}
cat << endofsnippet >> ${readme_filename}

The above content is the diff of
[step04_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step04_produce_output.py)
and
[step05_produce_output.py](https://github.com/researcherben/python-interfaces/blob/master/tutorial/step05_produce_output.py)

EOF

endofsnippet

# EOF
