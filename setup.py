#!/usr/bin/env python

"""The setup script."""

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['numpy>=1.15.4', 'sympy>=1.3']

test_requirements = ['pytest>=3', ]

setup(
    author="Jonny Comes",
    author_email='jonnycomes@gmail.com',
    name='look_and_say',
    version='0.1.1',
    python_requires='>=3.6',
    py_modules=['look_and_say'],
    license="MIT license",
    description="A python module for exploring look and say sequences in the spirit of John H Conway.",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='look_and_say',
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jonnycomes/look_and_say',
    project_urls={
        "Documentation": "https://jonnycomes.github.io/look_and_say/docs/",
        },
    zip_safe=False,
    )




