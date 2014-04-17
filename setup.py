from setuptools import setup

setup(
    name='awacs',
    version='0.3.2',
    description="AWS Access Policy Language creation library",
    author="Mark Peek",
    author_email="mark@peek.org",
    url="https://github.com/cloudtools/awacs",
    license="New BSD license",
    packages=['awacs'],
    test_suite="tests",
    use_2to3=True,
)
