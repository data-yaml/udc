.PHONY: install test watch coverage all clean

all: install test

clean:
	rm *coverage*

install:
	poetry install

test:
	poetry run pytest

watch:
	poetry run ptw --now .

coverage:
    poetry run pytest --cov --cov-report xml:coverage.xml
