"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='beame',
    version='0.0.1',

    description='Beame.io SDK - x509 certificates and tunnelling traffic to your servers',
    long_description=long_description,
    url='https://github.com/beameio/beame-sdk-python',
    author='beame.io',
    author_email='sophia@beame.io',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    # TODO: check about the comma separation
    keywords='beame, SSL cert, x509, localhost, proxy tunnel, ssl tunnel, self signed , CA, signing, crypto',
    packages=['beame']

    ### # List additional groups of dependencies here (e.g. development
    ### # dependencies). You can install these using the following syntax,
    ### # for example:
    ### # $ pip install -e .[dev,test]
    ### extras_require={
    ###     'dev': ['check-manifest'],
    ###     'test': ['coverage'],
    ### },
)
