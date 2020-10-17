.ONESHELL:
SHELL := /bin/bash

SRC = $(wildcard nbs/*.ipynb)

release: pypi
	sleep 5
	fastrelease_conda_package --upload_user fastai
	nbdev_bump_version

conda_release:
	fastrelease_conda_package --upload_user fastai

pypi: dist
	twine upload --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist

