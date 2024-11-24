.PHONY: build

test:
	bash check-syntax.sh
	python3 src/ct.py --version
	python3 src/ct.py --help

build:
	-bash build.sh

install:
	pip3 uninstall ct
	pip3 install -r requirements.txt
	pip3 install .
	ct --version
	ct --help

dev:
	bash dev.sh

clean:
	-docker stop cloud-tools
	-docker rm cloud-tools
	-docker image rm ubuntu-dev

api:
	bash -ex api.sh

rust:
	bash build.sh

docs:
	bash src/scripts/generate_docs.sh
