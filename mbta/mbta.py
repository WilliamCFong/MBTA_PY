# -*- coding: utf-8 -*-

from mbta.query_engine import engine

"""Main module."""

class MBTA(object):

    """The main MBTA object. Encapsulates all user-end interactions with mbta's
    official API."""

    def __init__(self, api_key):
        """Instantiates an MBTA instance.

        api_key: A string for authorizing connection to MBTA. If set to NONE
        a warning will be issued as MBTA severely limits query quotas.

        """
        self._engine = Engine(api_key)

    def vehicle(self, id):
        raise NotImplementedError

    def trip(self, id):
        raise NotImplementedError

    def service(self, id):
        raise NotImplementedError

    def schedule(self, **filters):
        # TODO Ensure that some filter must be set
        raise NotImplementedError

    def route(self, id):
        raise NotImplementedError

    def prediction(self, **filters):
        raise NotImplementedError

    def facility(self, id):
        raise NotImplementedError

    def alert(self, id):
        raise NotImplementedError
