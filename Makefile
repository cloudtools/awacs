.PHONY: test

PYDIRS=setup.py awacs examples tests tools

test:
	pycodestyle ${PYDIRS}
	pyflakes ${PYDIRS}
	python setup.py test
