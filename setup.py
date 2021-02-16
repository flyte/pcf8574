#  -*- coding: utf-8 -*-
"""
Setuptools script for the pcf8574 project.
"""

import os

from setuptools import setup


def required(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pcf8574",
    version="0.1.2",
    packages=("pcf8574",),
    package_data={"pcf8574": ["py.typed"]},
    scripts=[],
    entry_points={},
    setup_requires="pytest-runner",
    tests_require="pytest",
    install_requires=required("requirements.txt").split("\n"),
    test_suite="pytest",
    zip_safe=False,
    author="Ellis Percival",
    author_email="pcf8574@failcode.co.uk",
    description="Library for communication with PCF8574 IO expander over I2C",
    long_description=required("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Communications",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Networking",
    ],
    license="MIT",
    keywords="",
    url="https://github.com/flyte/pcf8574",
)
