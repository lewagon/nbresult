from setuptools import find_packages
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='nbresult',
      version='0.0.8',
      description='Extract results from Jupyter notebooks',
      license="MIT",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/lewagon/nbresult",
      author='Kevin Robert',
      author_email='kevin@lewagon.org',
      packages=find_packages(include=["nbresult"]),
      include_package_data=True
)
