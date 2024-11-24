#!/usr/bin/env python3
# Author: electronicsleep@gmail.com
# Purpose: Argparse for standalone scripts

# Usage
# python3 argparse.py -n test

import time
import argparse

# sys.path.append('../') # noqa
# import ct_lib # noqa

parser = argparse.ArgumentParser(description='CloudTools')
required = parser.add_argument_group('required arguemets')
optional = parser.add_argument_group('optional arguemets')
required.add_argument('-n', '--name', help='Name', required=False)
required.add_argument('-e', '--env', help='Env', required=False, default='qa')
optional.add_argument('-r', '--region', help='Region', required=False, default='us-west-1')
optional.add_argument('-t', '--test', help='Test', required=False, action='store_true')


args = vars(parser.parse_args())
name = args['name']
env = args['env']
region = args['region']
test = args['test']

time_now = time.strftime("%Y-%m-%d-%H%M%S")

print(f"name: {name} env: {env} region {region} time_now: {time_now}")
