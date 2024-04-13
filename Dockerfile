# Creative Commons Attribution 4.0 International License
# https://creativecommons.org/licenses/by/4.0/

# Use baseimage-docker which is a modified Ubuntu specifically for Docker
# https://hub.docker.com/r/phusion/baseimage
# https://github.com/phusion/baseimage-docker

# OLD!
#FROM phusion/baseimage:0.11

FROM phusion/baseimage:jammy-1.0.2@sha256:1584de70d2f34df8e2e21d2f59aa7b5ee75f3fd5e26c4f13155137b2d5478745

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# TODO: pin the apt package versions
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
    make \
    # sphinx is a pip package
    python3-pip

# TODO: build from offline cache - https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-local-archives
# TODO: build pip from source - https://pip.pypa.io/en/latest/cli/pip_install/#install-no-binary
# TODO: currently "requirements.txt" has pinned versions, but for reproducibility requirements.txt would have to include all the versions from "pip3 freeze" output. 

# trying to compile Python Black from source triggers a complaint that setuptools 59 is too old (69 is current).
RUN pip3 install --upgrade pip setuptools
COPY requirements.txt requirements.txt
# https://pip.pypa.io/en/latest/cli/pip_install/#install-no-binary
# the "--no-binary :all:" gets the source instead of wheel from pypi
#RUN pip3 install --no-binary :all: -r requirements.txt 
# disabled the "build from source" because some dependency requires Rust (?!)
RUN pip3 install -r requirements.txt 


WORKDIR /opt/

COPY completed_script/json_schema.py \
     completed_script/produce_output.py \
     completed_script/validate_graph.py \
     completed_script/validate_json_schema.py \
     /opt/


# see https://github.com/researcherben/sphinx-and-doxygen-tutorial-configuration

# https://www.doxygen.nl/manual/starting.html
RUN doxygen -g

# https://stackoverflow.com/questions/4755913/how-to-use-doxygen-to-create-uml-class-diagrams-from-c-source
RUN sed -i 's/^EXTRACT_ALL.*/EXTRACT_ALL = YES/' Doxyfile && \
    sed -i 's/^UML_LOOK.*/UML_LOOK = YES/' Doxyfile && \
    sed -i 's/^RECURSIVE.*/RECURSIVE = YES/' Doxyfile && \
    sed -i 's/^GENERATE_TREEVIEW.*/GENERATE_TREEVIEW = YES/' Doxyfile && \
    sed -i 's/^SOURCE_BROWSER.*/SOURCE_BROWSER = YES/' Doxyfile && \
    sed -i 's/^CALL_GRAPH.*/CALL_GRAPH = YES/' Doxyfile && \
    sed -i 's/^CALLER_GRAPH.*/CALLER_GRAPH = YES/' Doxyfile && \
    sed -i 's/^HIDE_UNDOC_RELATIONS.*/HIDE_UNDOC_RELATIONS = NO/' Doxyfile

RUN doxygen Doxyfile

WORKDIR /opt/latex/
RUN make

# end of Doxygen

WORKDIR /opt/

# sphinx documentation
ENV TZ=UTC
RUN sphinx-quickstart . --sep --project "py-interface" --author "Ben" --no-batchfile --quiet
RUN make latex
RUN make html
# https://github.com/nektos/act/issues/1853
#RUN TZ=UTC make html


WORKDIR /opt/source/
RUN sed -i '13 i .. automodule:: produce_output' index.rst
RUN sed -i '14 i     :members:' index.rst
RUN sed -i '15 i     :undoc-members:' index.rst
RUN sed -i '16 i     :show-inheritance:' index.rst

RUN sed -i "31 i    'sphinx.ext.doctest'," conf.py
RUN sed -i "31 i    'sphinx.ext.todo'," conf.py
RUN sed -i "31 i    'sphinx.ext.autosummary'," conf.py
RUN sed -i "31 i    'sphinx.ext.autodoc'," conf.py
RUN sed -i "31 i    'sphinx.ext.coverage'," conf.py
RUN sed -i "31 i    'sphinx.ext.mathjax'," conf.py
RUN sed -i "31 i    'sphinx.ext.viewcode'," conf.py
RUN sed -i "31 i    'sphinx.ext.githubpages'" conf.py

WORKDIR /opt/build/latex
RUN pdflatex py-interface
RUN pdflatex py-interface


WORKDIR /opt
