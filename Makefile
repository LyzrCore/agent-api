clean:
	rm -rf dist build *.egg-info

build:
	python setup.py sdist bdist_wheel

install:
	pip install -e .