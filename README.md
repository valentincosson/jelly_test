# jellysmack_test

## Installation

### Requirements

- Pipenv (for install it `pip install pipenv`)
- Python 3.9.x

> Note: Pipenv is used for virtualenv and dependency management.

### Install & contribute

This Project is black library for harmonize codestyle and improve readability.

- `Pipenv install --dev`

> Note: use `--dev` only for testing or development purpose, not in production

## Use the project

This project use a CLI for simplify common operations.

Just type `pipenv run python -m jellysmack_test [COMMAND]` for using CLI commands.

Available Commands:

- `init-db`   Init database with fixtures data (import provided data).
- `reset-db`  Reset the database.
- `run`       Run the API server.

> Example: for running the API server locally, type `pipenv run python -m jellysmack_test run`

## Tests

I tried to wirte a lot of test for increase code coverage.
To start the tests, just do `pipenv run pytest`

## Docs

If you run the server locally with the CLI Command* you can access the auto-documented API from fast-api and all the filters / pagination options via : http://localhost:8000/docs

*`pipenv run python -m jellysmack_test run`

## Notes

The test contains the 3 mandatory parts. I only knew FastApi ans SQLAlchemy by name, so it took me a little while to find my bearings and get familiar with them. I think it took me about 5-6 hours without considering the discovery of FastApi and SQLAlchemy.

I didn't do the optional part because I wanted to be able to turn in the project in less than two weeks by coding only on my personal time.
