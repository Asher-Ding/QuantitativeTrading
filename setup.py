import os
from setuptools import setup, find_packages

__version__ = '0.1.0'
requirements = open('requirements.txt').readlines() # read requirements

setup(
    name='quantitative_training',
    version= __version__,
    author= 'asher',
    author_email= 'asherding@icloud.com',
    description='initializing Quantitative',
    install_requires = requirements # install requirements
)
    