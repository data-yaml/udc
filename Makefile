sinclude .env # create from example.env
.PHONY: install test watch all clean

TEST_README=--codeblocks
ifeq ($(TEST_OS),windows-latest)
	TEST_README=''
endif

all: install update test

clean:
	rm -rf coverage*
	rm -f .coverage*
	rm -f etr_*.json

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

tag:
	git tag `poetry version | awk '{print $$2}'`
	git push --tags

pypi: clean clean-git
	poetry version
	poetry build
	poetry publish --dry-run
	make tag

clean-git:
	git branch | grep -v '*' | grep -v 'main' | xargs git branch -D

which:
	which udc
	udc --version

pip-install:
	python3 -m pip install udc
	make which

pip-upgrade:
	python3 -m pip install --upgrade udc
	make which


