# Creative Commons Attribution 4.0 International License
# https://creativecommons.org/licenses/by/4.0/

# this Makefile contains targets for use inside the Docker container and on the baremetal host

mytag=interface_demo

# what is available?
help:
	@echo "make help"
	@echo "      this message"
	@echo "make docker"
	@echo "         build and run"


# intended to be run on the host only
docker: docker_build docker_run
docker_build:
	time docker build -f Dockerfile -t $(mytag) .
docker_run:
	docker run -it -v `pwd`:/scratch --rm $(mytag) /bin/bash

# for reproducibility, which version of each dependency am I using?
# as per https://stackoverflow.com/a/42681459/1164295
docker_digest:
	docker images --digests


python_versions:
	docker run -it -v `pwd`:/scratch --rm interface_demo pip3 freeze > py_versions.log

# https://help.ubuntu.com/community/PinningHowto
apt_versions:

