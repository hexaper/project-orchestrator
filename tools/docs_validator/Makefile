.PHONY: install test validate clean

PYTHON ?= python3

install:
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest -v

validate:
	PYTHONPATH=src $(PYTHON) -m docs_validator.cli ../../docs ../../docs/_examples

clean:
	rm -rf build dist *.egg-info .pytest_cache __pycache__
