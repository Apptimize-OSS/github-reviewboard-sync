#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'GitPython',
    'PyGithub',
    'RBTools',
    'click',
    'giturlparse.py',
    'keyring',
    'six'
]

test_requirements = [
    'mock',
    'tox',
    'unittest2'
]

version = '0.1.4'

setup(
    name='github_reviewboard_sync',
    version=version,
    description='Syncs pull requests with ReviewBoard '
                'submissions allowing you to create a pull request '
                'and review board submission at the same time',
    long_description=readme + '\n\n' + history,
    author="Apptimize - Tim Martin",
    author_email='martin@apptimize.com',
    url='https://github.com/timmartin19/github_reviewboard_sync',
    packages=[
        'github_reviewboard_sync',
    ],
    package_dir={'github_reviewboard_sync':
                 'github_reviewboard_sync'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='github_reviewboard_sync',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'grs = github_reviewboard_sync.cli:cli'
        ]
    },
    extras_require={
        'release': ['zest.releaser']
    },
    test_suite='tests',
    tests_require=test_requirements
)
