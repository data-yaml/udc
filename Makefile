.PHONY: install test watch coverage all clean

all: install test

clean:
	rm *coverage*

install:
	poetry install

test:
	poetry run pytest --codeblocks --cov --cov-report xml:coverage.xml

watch:
	poetry run ptw --now .
