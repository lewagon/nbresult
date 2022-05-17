from setuptools import find_packages
from setuptools import setup

import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = [c.strip() for c in f.readlines()]

setup(name='nbresult',
      version='0.0.7',
      description='Extract results from Jupyter notebooks',
      license="MIT",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/lewagon/nbresult",
      author='Kevin Robert',
      author_email='kevin@lewagon.org',
      packages=find_packages(include=["nbresult"]),
      include_package_data=True,
      install_requires=requirements,
      scripts=[os.path.join("scripts", "nbresult_checker")])
