FILE_NAME=produce_output.py

help:
	@echo "make docker_shell"
	@echo "make pydeps"
	@echo "make mypy"
	@echo "        make docker_mypy"
	@echo "make unittest"
	@echo "make pytest"
	@echo "make pycallgraph"
	@echo "        make docker_pycallgraph"
	@echo "make prospector"
	@echo "make flake8"
	@echo "make black"
	@echo "make pylint"
	@echo "make doctest"
	@echo "        make docker_doctest"
	@echo "make mccabe"
	@echo "make clean"



docker_shell:
	docker run -it -v `pwd`:/scratch --workdir /scratch --rm interface_demo /bin/bash




pydeps:
	pydeps --no-show $(FILE_NAME)




# https://mypy.readthedocs.io/en/stable/
# Mypy is a static type checker
mypy:
	mypy --check-untyped-defs $(FILE_NAME)

docker_mypy:
	docker run -it -v `pwd`:/scratch --rm interface_demo mypy --check-untyped-defs /scratch/$(FILE_NAME)






# https://pypi.org/project/robotframework/
robot:
	robot test_robots/tests.robot






# https://behave.readthedocs.io/en/latest/
# https://github.com/behave/behave
# "behave is a behavior-driven (BDD) test framework that is very similar to Cucumber, Cucumber-JVM, and SpecFlow."
# https://automationpanda.com/2018/05/11/python-testing-101-behave/




# https://automationpanda.com/2017/03/10/python-testing-101-unittest/
unittest:
	python3 -m unittest discover




# https://automationpanda.com/2017/03/14/python-testing-101-pytest/
pytest:
	python3 -m pytest pytests/test_produce_output.py




# https://pycallgraph.readthedocs.io/en/master/
# creates call graph visualizations
pycallgraph:
	pycallgraph graphviz -- ./$(FILE_NAME) 4

docker_pycallgraph:
	docker run -it -v `pwd`:/scratch --rm interface_demo pycallgraph graphviz -- /scratch/$(FILE_NAME)




# http://prospector.landscape.io/en/master/
# analyze Python code and output information about errors, 
# potential problems, convention violations and complexity.
prospector:
	prospector
# as of 2024-04-13 prospector isn't working for me:
#     from pylint.config import find_pylintrc
# ImportError: cannot import name 'find_pylintrc' from 'pylint.config' (/usr/local/lib/python3.10/dist-packages/pylint/config/__init__.py)


# https://flake8.pycqa.org/en/latest/
# enforce style consistency across Python projects.
flake8:
	flake8 --ignore W291,E115,E121,E122,E124,E126,E127,E128,E203,E221,E225,E231,E241,E251,E261,E265,E302,E303,E501,E701
# E115 expected an indented block
# E121 continuation line under-indented for hanging indent
# E122 continuation line missing indentation or outdented
# E124 closing bracket does not match visual indentation
# E126 continuation line over-indented for hanging indent
# E127 Continuation line over-indented for visual indent; https://www.flake8rules.com/rules/E127.html
# E128 continuation line under-indented for visual indent
# E203 whitespace before
# E221 multiple spaces before operator
# E225 missing whitespace around operator
# E231 missing whitespace after ','
# E241 multiple spaces after ','
# E251 unexpected spaces around keyword / parameter equals
# E261 at least two spaces before inline comment
# E265 block comment should start with '# '
# E302 Expected 2 blank lines, found 0; https://www.flake8rules.com/rules/E302.html
# E303 too many blank lines
# E501 Line too long; https://www.flake8rules.com/rules/E501.html
# E701 Multiple statements on one line; https://www.flake8rules.com/rules/E701.html

# https://black.readthedocs.io/en/stable/
# By using Black, you agree to cede control over minutiae of hand-formatting.
black:
	black json_schema.py
	black $(FILE_NAME)
	black validate_graph.py
	black validate_json_schema.py





# https://www.pylint.org/
# http://pylint.pycqa.org/en/latest/
# checks for errors in Python code, tries to enforce a coding standard and looks for code smells.
pylint:
	pylint $(FILE_NAME)




# https://docs.python.org/3/library/doctest.html
# searches for pieces of text that look like interactive Python sessions, and 
# then executes those sessions to verify that they work exactly as shown.
doctest:
	python3 -m doctest -v $(FILE_NAME)

docker_doctest:
	docker run -it -v `pwd`:/scratch --rm interface_demo make -f /scratch/Makefile doctest FILE_NAME=produce_output.py 




# https://pypi.org/project/mccabe/
# check McCabe complexity; see
# https://en.wikipedia.org/wiki/Cyclomatic_complexity
mccabe:
	python3 -m mccabe $(FILE_NAME)




clean:
	rm -rf .mypy_cache __pycache__ logs *.json *.png *.svg

#EOF
