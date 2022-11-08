install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest vv main.py

format:
	black *.py


lint:
	pylint --disable=R,C searching_tweets.py

all: install lint test
