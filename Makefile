sinclude .env # create from example.env
.PHONY: install test watch all clean

TEST_README=--codeblocks
ifeq ($(TEST_OS),windows-latest)
	TEST_README=''
endif

all: install update test

clean:
	rm -rf coverage_html
	rm -f *coverage*

install:
	poetry install

update:
	poetry update

test:
	poetry run pytest $(TEST_README) --cov --cov-report xml:coverage.xml

coverage:
	poetry run pytest --cov --cov-report html:coverage_html
	open coverage_html/index.html

watch:
	poetry run ptw --now .
