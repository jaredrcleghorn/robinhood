import re
import requests
import uuid

def generate_device_token():
    return str(uuid.uuid4())

class Robinhood:
    __API_BASE_URL = 'https://api.robinhood.com'

    def __create_token(self, device_token, username, password, challenge_type=None, challenge_id=None):
        return requests.post(f'{self.__API_BASE_URL}/oauth2/token/', headers={
            'X-ROBINHOOD-CHALLENGE-RESPONSE-ID': challenge_id,
            'X-Robinhood-API-Version': '1.431.4',
        }, json={
            'grant_type': 'password',
            'client_id': 'c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS',
            'device_token': device_token,
            'challenge_type': challenge_type,
            'username': username,
            'password': password,
        })

    def __init__(self, device_token, username, password):
        r = self.__create_token(device_token, username, password)

        if r.status_code != 200:
            accept_challenge_types = tuple({
                'key': key,
                'value': value
            } for key, value in r.json()['accept_challenge_types'].items())

            print("Robinhood's sending you a code to verify your login. What is the best way to reach you?")
            print()

            for i, accept_challenge_type in enumerate(accept_challenge_types):
                print(f"{i + 1}. {accept_challenge_type['value']}")

            print()
            print('Please enter one of the numbers above: ', end='')

            challenge_type = accept_challenge_types[int(input()) - 1]['key']
            r = self.__create_token(device_token, username, password, challenge_type)
            challenge_id = r.json()['challenge']['id']

            print('Please enter the verification code Robinhood sent to you: ', end='')

            verification_code = input()

            requests.post(f'{self.__API_BASE_URL}/challenge/{challenge_id}/respond/', json={'response': verification_code})

            r = self.__create_token(device_token, username, password, challenge_id=challenge_id)

        token = r.json()
        self.__TOKEN = f"{token['token_type']} {token['access_token']}"

    def get_positions(self):
        r = requests.get(f'{self.__API_BASE_URL}/positions/?nonzero=true', headers={'Authorization': self.__TOKEN})
        positions = r.json()['results']
        instrument_ids = ','.join(tuple(re.search(f'{self.__API_BASE_URL}/positions/.+/(.+)/$', position['url']).group(1) for position in positions))
        r = requests.get(f"{self.__API_BASE_URL}/instruments/?active_instruments_only=false&ids={instrument_ids}", headers={'Authorization': self.__TOKEN})
        instruments = r.json()['results']

        return tuple({
            'symbol': instruments[i]['symbol'],
            'quantity': float(positions[i]['quantity']),
        } for i in range(len(positions)))

    def get_historicals(self, symbol):
        r = requests.get(f'{self.__API_BASE_URL}/marketdata/historicals/{symbol}/?bounds=regular&interval=day&span=year', headers={'Authorization': self.__TOKEN})
        historicals = r.json()['historicals']

        return tuple({
            'begins_at': re.search('^([0-9]{4}(-[0-9]{2}){2})', historical['begins_at']).group(1),
            'close_price': float(historical['close_price']),
        } for historical in historicals)
