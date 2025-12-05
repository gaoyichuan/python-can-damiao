# -*- coding: utf-8 -*-
"""
setup.py

python-can-damiao
"""

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="python-can-damiao",
    version="0.1.0",
    author="Yichuan Gao",
    author_email="i@gycis.me",
    description="Python-can Damiao USB-CAN adapter plugin",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gaoyichuan/python-can-damiao",
    py_modules=["damiao"],
    python_requires=">=3.9",
    install_requires=[
        "python-can",
        "pyserial>=3.5"
    ],
    entry_points={
        'can.interface': [
            'damiao = damiao:DamiaoBus'
        ]
    }
)
