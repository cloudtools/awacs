from setuptools import setup, find_packages

setup(
    name='awacs',
    version='0.6.1',
    description="AWS Access Policy Language creation library",
    author="Mark Peek",
    author_email="mark@peek.org",
    url="https://github.com/cloudtools/awacs",
    license="New BSD license",
    packages=find_packages(),
    test_suite="tests",
    use_2to3=True,
    requires=['slimit'],
)
