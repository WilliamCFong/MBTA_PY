# -*- coding: utf-8 -*-

from mbta.query_engine.engine import Engine
from mbta.vehicle.vehicle import Vehicle
from mbta.route.route import Route
from mbta.line.line import Line
from mbta.stops import Stop

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
        vehicle = self._engine.request(Vehicle.id_route, id)
        return Vehicle(**vehicle)

    def vehicles(self, **search_params):
        vehicles = self._engine.request(Vehicle.route, **search_params)
        return [Vehicle(**vehice) for vehicle in vehicles]

    def trip(self, id):
        self._engine.request('trip', id)

    def service(self, id):
        raise NotImplementedError

    def schedule(self, **filters):
        # TODO Ensure that some filter must be set
        raise NotImplementedError

    def stop(self, id):
        stop = self._engine.request(Stop.id_route, id)
        return Stop(**stop)

    def stops(self, **search_params):
        stops = self._engine(Stop.list_route, **search_params)
        return [Stop(**stop) for stop in stops]

    def route(self, id):
        route = self._engine.request(Route.id_route, id)
        return Route(**route)

    def routes(self, **search_params):
        routes = self._engine.request(Route.route, **search_params)
        return [Route(**route) for route in routes]

    def line(self, id):
        line = self._engine.request(Line.id_route, id)
        return Line(**line)

    def lines(self, **search_params):
        lines = self._engine.request(Line.route **search_params)
        return [Line(**line) for line in lines]

    def prediction(self, **filters):
        raise NotImplementedError

    def facility(self, id):
        raise NotImplementedError

    def alert(self, id):
        raise NotImplementedError
