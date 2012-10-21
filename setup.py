from setuptools import setup, find_packages

import django_wysiwyg

LONG_DESCRIPTION = open('README.rst').read()

setup(
    name='django-wysiwyg',
    version=django_wysiwyg.get_version(),
    description="django-wysiwyg",
    long_description=LONG_DESCRIPTION,
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
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Text Editors :: Word Processors",
        "Topic :: Text Processing :: Fonts",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    keywords='django,wysiwyg,redactor,ckeditor,',
    author=django_wysiwyg.__author__,
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/django-wysiwyg',
    license='MIT',
    packages=find_packages(exclude=('test_project',)),
    include_package_data=True,
    zip_safe=False
)
