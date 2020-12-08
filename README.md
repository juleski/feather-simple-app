# feather-simple-app

- Simple Flask API that allows user creation then facilitates simple insurance recommendation

## Requirements
- `docker-compose`
- python 3+

## Development
- You can either setup via `pipenv` or `make`

### Install dependencies via pipenv
- `pipenv install --dev`
- `pipenv shell` # to activate environment
- `pre-commit install` to setup git hook scripts

### Install dependencies via make
- `make install`
- `source .venv/bin/activate` # to activate environment
- `pre-commit install` to setup git hook scripts

## Running the app
- `docker-compose up &`

## Running the tests

### Unit tests
- `pytest -v -m unit`

### Integration tests
- `pytest -v -m integration`
> `NOTE`: When running integration tests the db should be up. Run it only via `docker-compose up db &`