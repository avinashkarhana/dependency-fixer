import codecs
import os
import sys
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="dependency-fixer",
    #name="dependency-fixer-avinashkarhana", #for test.pypi.org
    version=get_version("dependencyfixer/__init__.py"),
    author="Avinash Karhana",
    author_email="avinashkarhana1@gmail.com",
    description="A simple inscript multi-package installer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avinashkarhana/dependencyfixer",
    packages=find_packages(exclude="tests"),
    keywords=["dependencyfixer","dependencyhandler","dependency-fixer"], 
    install_requires=[
        "pip>=20.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)