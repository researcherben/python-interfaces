
help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets outside container ===="
	@echo "make docker"
	@echo "         build and run"
	@echo "==== Targets outside container ===="


docker: docker_build docker_run
docker_build:
	time docker build -f Dockerfile -t interface_demo .
docker_run:
	docker run -it -v `pwd`:/scratch --rm interface_demo /bin/bash

