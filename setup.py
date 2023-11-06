#!/usr/bin/env python

from setuptools import setup

setup(
    name="python-pushover2",
    version="0.5",
    description="Comprehensive bindings and command line utility for the "
    "Pushover notification service",
    long_description=open("README.rst").read()
    + "\n"
    + open("AUTHORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read(),
    url="https://github.com/Thibauth/python-pushover",
    author="Thibaut Horel, patched by m4rkw",
    author_email="thibaut.horel+pushover@gmail.com",
    py_modules=["pushover", "cli"],
    entry_points={"console_scripts": ["pushover = cli:main"]},
    install_requires=["requests>=1.0"],
    use_2to3=True,
    license="GNU GPLv3",
)
