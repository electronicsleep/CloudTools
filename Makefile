.PHONY: build

build:
	python3 src/ct.py --version
	python3 src/ct.py --help

check:
	bash check-syntax.sh
	python3 src/ct.py test

install:
	pip3 uninstall ct
	pip3 install -r requirements.txt
	pip3 install .
	ct --version
	ct --help

dev:
	bash dev.sh

clean:
	-docker stop CloudTools
	-docker rm CloudTools
	-docker image rm ubuntu-dev

api:
	bash -ex api.sh

rust:
	bash build.sh

docs:
	bash src/scripts/generate_docs.sh
