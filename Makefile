install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m searching_tweets.py

format:
	black *.py


lint:
	pylint --disable=R,C searching_tweets.py

all: install lint test
