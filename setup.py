#!/usr/bin/env python
'''
# Module: setup.py
'''

from setuptools import setup, find_packages

setup(
    name='solairesays',
    url='http://github.com/CharlieMartell/SolaireSays',
    author='Charlie Martell',
    author_email='charliecmartell@gmail.com',
    description = ("Some quotes from all your favorite Dark Souls NPC's"),
    packages=find_packages(
        exclude=(
            '.*',
            'EGG-INFO',
            '*.egg-info',
            '_trial*',
            '*.tests',
            '*.tests.*',
            'tests.*',
            'tests',
            'examples.*',
            'examples*',
            )
        ),
    entry_points = {
        'console_scripts': [
            'solairesays = solairesays:main'
        ]
    }
)
