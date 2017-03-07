import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-rq-wrapper',
    version='2.0',
    author='ISL',
    author_email='dev@isl.co',
    description=('Django management command to run multiple rq workers in one command and autoreload.'),
    license='MIT',
    keywords='django rq autoreload worker',
    url='https://github.com/istrategylabs/django-rq-wrapper',
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=['django>=1.8.0', 'rq>=0.5.5', 'django-rq>=0.9.2'],
)
