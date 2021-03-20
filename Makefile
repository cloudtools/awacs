.PHONY: test

PYDIRS=setup.py awacs examples tests

test:
	pycodestyle ${PYDIRS}
	pyflakes ${PYDIRS}
	python setup.py test
