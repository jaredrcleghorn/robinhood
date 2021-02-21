import json
import os
import robinhood as rh

CONFIG_FILENAME = 'config.json'

with open(CONFIG_FILENAME) as f:
    config = json.load(f)

device_token = config['device_token'] or os.environ.get('ROBINHOOD_DEVICE_TOKEN')

if device_token == None:
    device_token = rh.generate_device_token()
    username = config['username'] or os.environ.get('ROBINHOOD_USERNAME')
    password = config['password'] or os.environ.get('ROBINHOOD_PASSWORD')

    print()
    rh.Robinhood(device_token, username, password)
    print()

    config['device_token'] = device_token

    with open(CONFIG_FILENAME, 'w') as f:
        json.dump(config, f, indent='\t')
        f.write('\n')
