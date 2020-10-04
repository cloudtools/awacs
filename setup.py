import os
from setuptools import setup, find_packages

# ----------------------------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------------------------


def file_contents(file_name):
    """Given a file name to a valid file returns the file object."""
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(curr_dir, file_name)) as the_file:
        contents = the_file.read()
    return contents


def get_version():
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    with open(curr_dir + "/awacs/__init__.py", "r") as init_version:
        for line in init_version:
            if "__version__" in line:
                return str(line.split("=")[-1].strip(" ")[1:-2])

# ----------------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------------


setup(
    name='awacs',
    version=get_version(),
    description="AWS Access Policy Language creation library",
    long_description=file_contents("README.rst"),
    long_description_content_type='text/x-rst',

    author="Mark Peek",
    author_email="mark@peek.org",
    url="https://github.com/cloudtools/awacs",
    license="New BSD license",
    packages=find_packages(),
    test_suite="tests",
    use_2to3=True,
    requires=['slimit'],
    python_requires=(
        ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*"
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",

        "License :: OSI Approved :: BSD License",

        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",

        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 2.7",
    ],
)
