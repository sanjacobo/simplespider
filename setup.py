import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="spidertest",
    version='0.9.2',
    author="Santiago Guichon",
    author_email="santiago.guichon@gmail.com",
    description="Spider Scrapy",
    # packages=['an_example_pypi_project', 'tests'],
    packages=find_packages(),
    entry_points={'scrapy': ['settings = spider_test.settings']},
    install_requires=[
        'pyasn1-modules',
        'scrapy==1.4.0',
    ]
)
