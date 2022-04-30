#!/usr/bin/env python

from setuptools import setup

setup(name='ct',
      version='1.0',
      description='CloudTools - Example Python Cloud Tools template using Typer/Fastapi',
      author='Chris https://github.com/electronicsleep',
      url='https://github.com/electronicsleep/CloudTools',
      install_requres=["typer==0.3.2", "typer-cli==0.0.11"],
      package_dir={'': 'src'},
      entry_points={
        'console_scripts': ['ct=ct:main']
      }
)
