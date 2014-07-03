#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import codecs
import os
import re
import sys


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_variable(variable, *parts):
    version_file = read(*parts)
    version_match = re.search(r"^{0} = ['\"]([^'\"]*)['\"]".format(variable), version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-wysiwyg',
    version=find_variable('__version__', 'django_wysiwyg', '__init__.py'),
    description="django-wysiwyg",
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Editors :: Word Processors",
        "Topic :: Text Processing :: Fonts",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    keywords='django,wysiwyg,redactor,ckeditor,tinymce,froala',
    author=find_variable('__author__', 'django_wysiwyg', '__init__.py'),
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/django-wysiwyg',
    license='MIT',
    packages=find_packages(exclude=('test_project*',)),
    include_package_data=True,
    zip_safe=False
)
