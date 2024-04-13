# Creative Commons Attribution 4.0 International License
# https://creativecommons.org/licenses/by/4.0/

# this Makefile contains targets for use inside the Docker container and on the baremetal host

mytag=interface_demo

# what is available?
help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets outside container ===="
	@echo "make docker"
	@echo "         build and run"
	@echo "==== Targets inside container ===="
	@echo "make doctest"
	@echo "make mypy"


# the following targets are intended to be run inside the Docker container
hello:
	g++ hello_world.cpp


