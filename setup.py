#!/usr/bin/env python

from setuptools import setup, find_packages

tests_require = [
    'pytest',
    'unittest2',
]

setup(
    name='reraise',
    version='0.2.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/reraise',
    description='Reraise exceptions, like a boss.',
    long_description=__doc__,
    packages=find_packages(),
    license='Apache 2.0',
    zip_safe=False,
    extras_require={
        'tests': tests_require,
    },
    install_requires=['six'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
