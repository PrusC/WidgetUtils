#
# @File: setup.py.py
#
# Author: Konstantin Prusakov <konstatnin.prusakov@phystech.edu>
#

from setuptools import setup, find_packages

__version__ = 0.9

setup(
    name='WidgetUtils',
    version=__version__,
    description='Some useful things',
    author='Konstantin Prusakov',
    author_email='konstatnin.prusakov@phystech.edu',
    # package_dir={"WidgetUtils": "."},
    # packages=find_packages(where='..', exclude='test.py'),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'opencv-python',
        'PySide2',
    ],
)
