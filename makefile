all: install build publish

install:
	pip install \
		-e .[test,dev]

test: lint
	pytest

cov: test
	coverage html

build: clean test
	python setup.py sdist

clean: setup.py setup.cfg
	rm -rf dist/
	rm -rf .eggs/
	rm -rf fastapi-demo.egg-info/
	@echo "Cleaned up previous builds."

publish:
	@echo "Attempting publish. Must run \`make build\` before this."
	twine upload --config-file ~/.pypirc --repository xyz --verbose dist/*

lint:
	flake8

black:
	black .