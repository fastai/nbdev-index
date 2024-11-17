.ONESHELL:
SHELL := /bin/bash

SRC = $(wildcard nbs/*.ipynb)

release: pypi
	sleep 5
	nbdev_bump_version

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist

