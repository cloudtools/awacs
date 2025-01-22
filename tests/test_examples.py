import glob
import os
import pytest
import sys


files = glob.glob(os.path.join("examples", "*.py"))


@pytest.mark.parametrize("filename", files)
def test_file(filename):
    # Ignore the output
    saved = sys.stdout
    with open("/dev/null", "w") as stdout:
        sys.stdout = stdout
        try:
            with open(filename) as f:
                code = compile(f.read(), filename, "exec")
                exec(code)
        finally:
            sys.stdout = saved
