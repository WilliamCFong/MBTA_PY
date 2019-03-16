import requests
from mbta.exceptions import MBTA_NotFound, MBTA_Forbidden, MBTA_QuotaExceeded, MBTA_Exception

RESPONSE_KEYS = ['id', 'attributes', 'relationships']

def construct_filters(**filters):
    """Wraps filter parameter keys to be 'filter[key]': value"""
    keys = filters.keys()
    return {f'filter[{key}]': filters[key] for key in keys}

def require_filters(*required_filters, **passed_filters):
    passed_keys = set(filters.keys())
    check = passed_keys.intersection(set(required_filters))
    if not check:
        message = f'{required_filters} not present in:\n'
        for key in passed_keys:
            message += f'\t{key}: {passed_filters[key]}\n'
        raise KeyError(message)

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
        r = requests.get(
            url,
            headers=self._headers,
            params=construct_filters(**params)
        )
        response = r.json()

        if r.status_code == 200:
            x = { key: response['data'][key] for key in RESPONSE_KEYS if key in response['data'] }
            return x
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

