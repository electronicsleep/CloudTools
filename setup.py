#!/usr/bin/env python

from setuptools import setup

setup(name='ct',
      version='1.0',
      description='CloudTools - Example Python Cloud Tools template using Typer/Fastapi',
      author='Chris https://github.com/electronicsleep',
      url='https://github.com/electronicsleep/CloudTools',
      package_dir={'': 'src'},
      entry_points={
        'console_scripts': ['ct=ct:main']
      }
)
