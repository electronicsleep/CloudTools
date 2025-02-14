#!/usr/bin/env python

from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name="ct",
      version="0.3.4",
      description="CloudTools - Example Python/Rust Tools using Typer/Fastapi",
      py_modules=["ct", "ct_lib", "ct_inv", "ct_rust", "ct_kube"],
      exclude_package_data={"scripts": ["scripts"]},
      author="https://github.com/electronicsleep",
      url="https://github.com/electronicsleep/CloudTools",
      install_requres=required,
      package_dir={"": "src"},
      entry_points={
          "console_scripts": ["ct=ct:app"]
      })
