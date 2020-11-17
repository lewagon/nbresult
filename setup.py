from setuptools import find_packages
from setuptools import setup

setup(
    name='nbresult',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    description='Extract results from Jupyter notebooks'
)
