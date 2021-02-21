# robinhood

[![GitHub](https://img.shields.io/github/license/jaredrcleghorn/robinhood?color=blue)](https://github.com/jaredrcleghorn/robinhood/blob/main/LICENSE)
![publish](https://github.com/jaredrcleghorn/robinhood/actions/workflows/publish.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/jc.robinhood)](https://pypi.org/project/jc.robinhood/)

Unofficial Robinhood API client library for Python

## Installation

```shell
pipenv install jc.robinhood
```

## Usage

```python
import json
import robinhood as rh

CONFIG_FILENAME = 'config.json'

with open(CONFIG_FILENAME) as f:
    config = json.load(f)

device_token = config['robinhood']['device_token']
username = config['robinhood']['username']
password = config['robinhood']['password']

if device_token == '':
    device_token = rh.generate_device_token()

    print()
    robinhood = rh.Robinhood(device_token, username, password)

    config['robinhood']['device_token'] = device_token

    with open(CONFIG_FILENAME, 'w') as f:
        json.dump(config, f, indent='\t')
        f.write('\n')
else:
    robinhood = rh.Robinhood(device_token, username, password)

print()
print('Positions:')
print()

for position in robinhood.get_positions():
    print(f"{position['symbol']} ({position['quantity']})")

print()
```

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
