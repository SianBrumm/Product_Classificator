from setuptools import setup, find_packages

setup(
    name='product-classificator',
    version='0.1',
    packages=find_packages(),
    package_data={
        'product-classificator': ['data/keywords.json']
    }
)