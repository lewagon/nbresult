default: pylint pytest

pylint:
	find . -iname "*.py" -not -path "./tests/test_*" | xargs -n1 -I {}  pylint --output-format=colorized {}; true

pytest:
	PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes tests/test_challenge_result.py

build:
	rm -rf build
	rm -rf dist
	python setup.py sdist bdist_wheel

push_to_testpypi:
	twine upload --repository testpypi dist/*

install_from_testpypi:
	python -m pip install --index-url https://test.pypi.org/simple/ nbresult

publish:
	twine upload dist/*
