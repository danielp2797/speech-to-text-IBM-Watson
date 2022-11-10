from setuptools import find_packages, setup

setup(
    name='src',
    author='Daniel Perez',
    packages=find_packages(include=['src', 'src.*'])
)
