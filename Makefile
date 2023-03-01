install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

download:
	python -m spacy download en_core_web_sm

test:
	python -m pytest -vv main.py

format:
	black *.py

lint:
	pylint --disable=R,C,protected-access *.py

all: install lint test
