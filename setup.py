# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="ExoPSI",
    version="0.1.7",
    description="Library to calculate Similarity Indexes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ExoPSI/ExoPSI",
    author="Aditya Rai",
    author_email="rai.aditya01@gmail.com",
    license="GNU GPL v3.0",
    classifiers=[
        "Intended Audience :: Developers",  
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["ExoPSI"],
    include_package_data=True,
    install_requires=["numpy","matplotlib","pandas"]
)