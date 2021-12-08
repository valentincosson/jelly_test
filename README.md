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

### Routes

You can use filters on each fields (*except id and create/update dates*) on List Characters and List Comments.
Pagination is also available on this same routes with `offset` and `limit` filters.

#### Character

[GET]
`/character/`
*List Characters*

[GET]
`/character/{item_id}`
*Read Character*

#### Episode

[GET]
`/episode/`
*List Episodes*

[GET]
`/episode/{item_id}`
*Read Episode**

#### Comment

[GET]
`/comment/`
*List Comments*

[POST]
`/comment/`
*Create Comment*

[GET]
`/comment/{item_id}`
*Read Comment*

[DELETE]
`/comment/{item_id}*`
*Delete Comment

[PATCH]
`/comment/{item_id}`
*Update Comment*

## Notes

The test contains the 3 mandatory parts. I only knew FastApi ans SQLAlchemy by name, so it took me a little while to find my bearings and get familiar with them. I think it took me about 5-6 hours without considering the discovery of FastApi and SQLAlchemy.

I didn't do the optional part because I wanted to be able to turn in the project in less than two weeks by coding only on my personal time.
