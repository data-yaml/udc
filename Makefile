.PHONY: install test watch all clean

TEST_README=--codeblocks
ifeq ($(TEST_OS),windows-latest)
	TEST_README=''
endif

all: install update test

clean:
	rm *coverage*

install:
	poetry install

update:
	poetry update

test:
	poetry run pytest $(TEST_README) --cov --cov-report xml:coverage.xml

watch:
	poetry run ptw --now .
