__author__ = 'ksaric'

import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Galileo',
    version='1.0',
    description="""This is a module for consuming NMAP scan results and serving them as a REST service
                  and as a web application.""",
    long_description=read('README.md'),
    packages=['galileo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=required
)
