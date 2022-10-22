#!/usr/bin/env python

from setuptools import setup

setup(name='ct',
      version='0.3.1',
      description='CloudTools - Example Python/Rust Tools using Typer/Fastapi',
      py_modules=['ct', "ct_lib", "ct_inv", "ct_rust"],
      exclude_package_data={"scripts": ["scripts"]},
      author='https://github.com/electronicsleep',
      url='https://github.com/electronicsleep/CloudTools',
      install_requres=["typer==0.3.2", "typer-cli==0.0.11"],
      package_dir={'': 'src'},
      entry_points={
        'console_scripts': ['ct=ct:main']
      }
)
