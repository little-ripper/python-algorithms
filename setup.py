from setuptools import setup, find_packages

__component_name__ = "python algorithms"
__author__ = "me"
__version__ = "0.0.1"
__description__ = "-*- Some Algorithms Quite interesting -*-"
__long_description__ = """"""

setup(
    name=__component_name__,
    version=__version__,
    author=__author__,
    long_description=__long_description__ if __long_description__ else __description__,
    packages=find_packages(where="."),
    package_dir={"": "."},
)
