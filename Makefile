.PHONY: build
build:
	bash -ex build.sh

install:
	pip3 install .

test: build
	python3 src/ct.py --version
	python3 src/ct.py --help

uninstall:
	pip3 uninstall ct

api:
	bash -ex run_api.sh
