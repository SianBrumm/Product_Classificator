from setuptools import setup

setup(
    name='product-classificator',
    version='0.1',
    packages=['classificator'],
    package_dir={'classificator': 'classificator'},
    package_data={'classificator': ['data/*.dat']},
)