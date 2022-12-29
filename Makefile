.PHONY: build
build:
	bash -ex build.sh

install:
	pip3 install .

test: build
	cd src; python3 ct.py --version
	cd src; python3 ct.py --help

uninstall:
	pip3 uninstall ct

api:
	bash -ex run_api.sh
