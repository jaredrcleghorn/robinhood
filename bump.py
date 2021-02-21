import json
import os
import requests

r = requests.get('https://pypi.org/pypi/jc.robinhood/json')
current_version = r.json()['info']['version']

os.system(f'bump2version --current-version {current_version} patch')
