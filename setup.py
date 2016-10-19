"""setup."""

import sys

from setuptools import find_packages
from setuptools import setup

sys.path.append('./src')
sys.path.append('./test')

setup(
    name="Takamari",
    version="0.1",
    packages=find_packages(),
    test_suite='test_hello.suite'
)
