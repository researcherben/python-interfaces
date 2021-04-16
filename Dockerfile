
# Use baseimage-docker which is a modified Ubuntu specifically for Docker
# https://hub.docker.com/r/phusion/baseimage
# https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:0.11

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Update and install packages
RUN apt update && apt -y upgrade && apt -y install \
    doxygen \
    python3 \
    # doxygen uses "dot" to make graphs
    graphviz \ 
    # doxygen PDF requires latex
    texlive-latex-base \
    texlive-latex-recommended texlive-pictures texlive-latex-extra \
    # doxygen latex requires make
    make 

WORKDIR /opt/

COPY json_schema.py \
     produce_output.py \
     solve.py \
     validate_graph.py \
     validate_json_schema.py \
     /opt/

# https://www.doxygen.nl/manual/starting.html
RUN doxygen -g

# https://stackoverflow.com/questions/4755913/how-to-use-doxygen-to-create-uml-class-diagrams-from-c-source
RUN cat Doxyfile | \
    sed 's/^EXTRACT_ALL.*/EXTRACT_ALL = YES/' | \
    sed 's/^UML_LOOK.*/UML_LOOK = YES/' | \
    sed 's/^RECURSIVE.*/RECURSIVE = YES/' | \
    sed 's/^GENERATE_TREEVIEW.*/GENERATE_TREEVIEW = YES/' | \
    sed 's/^SOURCE_BROWSER.*/SOURCE_BROWSER = YES/' | \
    sed 's/^CALL_GRAPH.*/CALL_GRAPH = YES/' | \
    sed 's/^CALLER_GRAPH.*/CALLER_GRAPH = YES/' | \
    sed 's/^HIDE_UNDOC_RELATIONS.*/HIDE_UNDOC_RELATIONS = NO/' > Doxyfile

RUN doxygen Doxyfile

WORKDIR /opt/latex/
RUN make

WORKDIR /opt/
