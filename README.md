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

- `init-db`   Init database with fixtures data.
- `reset-db`  Reset the database.
- `run`       Run the API server.

> Example: for running the API server locally, type `pipenv run python -m jellysmack_test run`

## Tests

To start the tests, just do `pipenv run pytest`
