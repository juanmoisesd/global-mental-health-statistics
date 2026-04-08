.PHONY: install test run

install:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	bash run.sh
