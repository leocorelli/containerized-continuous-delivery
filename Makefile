install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv test_logic.py test_app.py

format:
	black *.py

all: install test format