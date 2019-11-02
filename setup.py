#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name="tprint",
    version="1.0",
    description="Print python collections as tables",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tim Fischer",
    author_email="tim.fischer98@hotmail.com",
    url="https://github.com/tim-fi/tprint",
    py_modules=["tprint"],
    package_data={"": ["LICENSE"]},
    package_dir={"tprint": "tprint"},
    include_package_data=True,
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ]
)
