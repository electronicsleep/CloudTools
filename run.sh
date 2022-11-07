#!/bin/bash
pip3 install -r requirements.txt
cd src
python3 ct.py --version
python3 ct.py --help
python3 ct.py test
