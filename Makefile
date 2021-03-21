.PHONY: test

PYDIRS=setup.py awacs examples tests
PYVERSION=`python -c "import sys; print(''.join([str(sys.version_info.major), str(sys.version_info.minor)]))"`

test:
	python -m tox -e qa
	python -m tox -e package
	python -m tox --listenvs | grep "^py${PYVERSION}" | tr "\n" "," | xargs python -m tox -e
	black --check ${PYDIRS}
