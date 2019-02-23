import requests
from mbta.exceptions import MBTA_NotFound, MBTA_Forbidden, MBTA_QuotaExceeded, MBTA_Exception

class Engine(object):

    """A class for encapsulating API requests to MBTA. Requires credentials."""

    def __init__(self, api_key, base_url='https://api-v3.mbta.com'):
        self._api_key = api_key
        self._headers = {
            'x-api-key': api_key,
            'user-agent': 'MBTA.PY V0.1'
        }

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        raise ValueError(
            'Cannot set Engine API Key after instantiation.'
        )

    @property
    def user_agent(self):
        return self._headers['user-agent']

    @user_agent.setter
    def user_agent(self, user_agent):
        self._headers['user-agent'] = user_agent

    def request(self, *route, **params):
        url = '/'.join(route)
        r = requests.get(url, headers=self._headers, params=params)
        response = r.json()

        if r.status_code == 200:
            return response
        elif r.status_code == 403:
            raise MBTA_Forbidden(url)
        elif r.status_code == 404:
            raise MBTA_NotFound(response, params)
        elif r.status_code == 429:
            raise MBTA_QuotaExceeded()
        else:
            raise MBTA_Exception(
                f'Error in getting response from {url}.'
                ' Returned {r.status_code} and {response}'
            )

