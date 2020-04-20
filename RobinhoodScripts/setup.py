from setuptools import setup

with open('README.md', 'r') as readmeFile:
    long_description = readmeFile.read()

setup(
    name = 'autohood',
    version = '0.1.0',
    description = 'A module that utilizes robin_stocks',
    liscense = 'MIT',
    long_description = long_description,
    author = 'John Fahey',
    author_email = 'JGFahey@gmail.com',
    packages = ['autohood'],
    install_requires = ['robin_stocks']
    entry_points = {
        'console_scripts': ['autohood = autohood.__main__:main']
    }
)