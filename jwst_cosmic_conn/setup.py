#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Vineeth Aljapur",
    author_email='vineethaljapur@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Contains application of cosmic-conce Telescope",
    entry_points={
        'console_scripts': [
            'jwst_cosmic_conn=jwst_cosmic_conn.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='jwst_cosmic_conn',
    name='jwst_cosmic_conn',
    packages=find_packages(include=['jwst_cosmic_conn', 'jwst_cosmic_conn.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/VineethAljapur/jwst_cosmic_conn',
    version='0.1.0',
    zip_safe=False,
)
