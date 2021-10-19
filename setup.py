from setuptools import setup, find_packages

setup(
    name="transouest",
    version="1.0",
    packages=find_packages(exclude=("unittests",)),
    install_requires=[
        "black",
        "coverage",
        "pip-tools",
        "pandas",
        "openpyxl",
    ],
)
