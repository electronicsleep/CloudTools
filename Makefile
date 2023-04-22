.PHONY: build

test:
	pip3 install -r requirements.txt
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

api:
	bash -ex run_api.sh
