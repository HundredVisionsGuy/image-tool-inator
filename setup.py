#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Hundred Visions Guy",
    author_email='cwinikka@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A set of image processing libraries that I will build over the years as I think of things to do - don't stay up waiting for version 1.0",
    entry_points={
        'console_scripts': [
            'image_tool_inator=image_tool_inator.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='image_tool_inator',
    name='image_tool_inator',
    packages=find_packages(include=['image_tool_inator', 'image_tool_inator.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hundredvisionsguy/image_tool_inator',
    version='0.1.0',
    zip_safe=False,
)
