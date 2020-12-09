from setuptools import find_packages
from setuptools import setup

setup(
    name='nbresult',
    description='Extract results from Jupyter notebooks',
    version='0.0.1',
    author='Kevin Robert',
    author_email='kevin@lewagon.org',
    packages=find_packages(),
    include_package_data=True
)
