#  -*- coding: utf-8 -*-
"""
Setuptools script for the pcf8574 project.
"""

import os
from textwrap import fill, dedent

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def required(fname):
    return open(
        os.path.join(
            os.path.dirname(__file__), fname
        )
    ).read().split('\n')


setup(
    name="pcf8574",
    version="0.0.4",
    packages=("pcf8574",),
    scripts=[],
    entry_points={},
    include_package_data=True,
    setup_requires='pytest-runner',
    tests_require='pytest',
    install_requires=required('requirements.txt'),
    test_suite='pytest',
    zip_safe=False,
    # Metadata for upload to PyPI
    author='Ellis Percival',
    author_email="pcf8574@failcode.co.uk",
    description="Library for communication with PCF8574 IO expander over I2C",
    long_description=fill(dedent("""\
        This is a library which can be used to communicate with one or many
        pcf8574 IO expander ICs over an I2C interface.
    """)),
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Communications",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Networking"
    ],
    license="MIT",
    keywords="",
    url="https://github.com/flyte/pcf8574"
)
