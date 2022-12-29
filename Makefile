.PHONY: build
build:
	bash -ex build.sh

version: build
	cd src; python3 ct.py --help
	cd src; python3 ct.py --version

test: build
	cd src; python3 ct.py cs
	cd src; python3 ct.py aws -c li

install:
	pip3 install .

uninstall:
	pip3 uninstall ct

api:
	bash -ex run_api.sh
