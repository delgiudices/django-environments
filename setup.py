#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of django-environments.
# https://github.com/delgiudices/django-environments

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Luis Del Giudice <luis.dg19@gmail.com>

from setuptools import setup, find_packages
from django_environments import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='django-environments',
    version=__version__,
    description='an incredible python package',
    long_description='''
an incredible python package
''',
    keywords='django deploy automatic deployment ubuntu nginx upstart',
    author='Luis Del Giudice',
    author_email='luis.dg19@gmail.com',
    url='https://github.com/delgiudices/django-environments',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'django-environments=django_environments.cli:main',
        ],
    },
)
