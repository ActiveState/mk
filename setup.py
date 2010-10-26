from setuptools import setup, find_packages
import sys, os
from os import path


# make sure that we import mklib/ (and not the system-wide one)
sys.path.insert(0, path.abspath(path.dirname(__file__)))
import mklib


setup(
    name='mk',
    version=mklib.__version__,
    description="a Makefile/make replacement written in Python (used at ActiveState)",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='make mk',
    author='Trent Mick',
    author_email='trentm@gmail.com',
    url='http://github.com/ActiveState/mk',
    license='MIT',
    packages=find_packages(exclude=[
        'examples', 'test']),
    include_package_data=True,
    zip_safe=False,
    entry_points={
      'console_scripts': [
          'mk=mklib.runner:main'
      ]
    },
)
