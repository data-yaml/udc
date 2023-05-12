install:
	poetry install

test:
	poetry run pytest

watch:
	poetry run ptw --onpass "say passed" --onfail "say failed"

