from setuptools import setup, find_packages

version = '0.1.0'

LONG_DESCRIPTION = """
=====================================
django_wysiwyg
=====================================
Django WYSIWYG is a django application that lets you easily change textareas
into rich text editors.
"""

setup(
    name='django-wysiwyg',
    version=version,
    description="django-wysiwyg",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='pinax,django',
    author='Daniel Greenfeld, Chris Adams',
    author_email='pydanny@gmail.com',
    url='',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    setup_requires=['setuptools_git'],
)