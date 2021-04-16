
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
RUN doxygen Doxyfile
