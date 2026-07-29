.PHONY: run test clean setup

run:
	python src/main.py

test:
	pytest tests/ -v

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	rm -rf .pytest_cache

setup:
	pip install -r requirements.txt

lint:
	python -m py_compile src/*.py tests/*.py
