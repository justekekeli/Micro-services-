install:
	pip install --upgrade pip &&\
			pip install -r requirements.txt

lint:
	pylint --disable=R,C,W103,W0702 main.py

test:
	python -m pytest -vv --cov=app test_app.py

format:
	black *.py