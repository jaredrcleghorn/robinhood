# robinhood

[![GitHub](https://img.shields.io/github/license/jaredrcleghorn/robinhood?color=blue)](https://github.com/jaredrcleghorn/robinhood/blob/main/LICENSE)
![test](https://github.com/jaredrcleghorn/robinhood/actions/workflows/test.yml/badge.svg)

Unofficial Robinhood API client library for Python

## Contributing

You will need [Pipenv](https://pipenv.pypa.io/en/latest/). On [Mac](https://www.apple.com/mac/), you
can install Pipenv using [Homebrew](https://brew.sh). To install Homebrew, run

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then, to install Pipenv, run

```shell
brew install pipenv
```

To install dependencies, move into the project folder and run

```shell
pipenv install
```

To run tests, fill out the `config.json` file with your Robinhood
`username` and `password` and then run

```shell
pipenv run test
```
