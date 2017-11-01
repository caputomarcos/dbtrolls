#!/usr/bin/env python

from setuptools import setup, find_packages

setup_requires = []

install_requires = ['pyyaml']

dev_requires = [
    'mock==2.0.0',
]


setup(
    name='dbtrolls',
    version='v1.0',
    author='Marcos Caputo <caputo.marcos@gmail.com>',
    url='https://github.com/caputomarcos/dbtrolls',
    description="dbtrolls - Rest Api Server using Dijsktra's algorithm applied to travelling salesman problem.",
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['docs', ]),
    zip_safe=True,
    install_requires=install_requires,
    extras_require={
        'dev': install_requires + dev_requires,
    },
    license='MIT',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'dbtrolls = dbtrolls.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python',
    ],
)
