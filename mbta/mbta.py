# -*- coding: utf-8 -*-

from mbta.query_engine.engine import Engine
from mbta.vehicle.vehicle import Vehicle
from mbta.route.route import Route
from mbta.line.line import Line
from mbta.stops import Stop
from mbta.schedule.schedule import Schedule
from mbta.trip.trip import Trip
from mbta.prediction.prediction import Prediction

from mbta.query_engine.engine import require_filters


"""Main module."""

class MBTA(object):

    """The main MBTA object. Encapsulates all user-end interactions with mbta's
    official API."""

    def __init__(self, api_key=None):
        """Instantiates an MBTA instance.
        Args:
            api_key optional: A string for authorizing connection to MBTA.
                If set to NONE MBTA will be set to Anonymouse Mode

        """
        self._engine = Engine(api_key)
        self._mode = True if api_key else False

    @property
    def in_anonymous_mode(self):
        return self._mode

    def vehicle(self, id):
        vehicle = self._engine.request(Vehicle.id_route, id)
        return Vehicle(**vehicle)

    def vehicles(self, **search_params):
        vehicles = self._engine.request(Vehicle.route, **search_params)
        return [Vehicle(**vehice) for vehicle in vehicles]

    def trip(self, id):
        trip = self._engine.request(Trip.id_route, id)
        return Trip(**trip)

    def trips(self, **filters):
        require_filters('date', 'direction_id', 'route', 'id', **filters)
        trips = self._engine.request(Trip.list_route, **filters)
        return [Trip(**trip) for trip in trips]

    def service(self, id):
        raise NotImplementedError

    def schedules(self, **filters):
        require_filters('route', 'stop', 'trip', **filters)
        schedules = self._engine.request(Schedule.list_route, **filters)
        return [Schedule(**schedule) for schedule in schedules]

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
        if self.in_anonymous_mode:
            raise AttributeError('Cannot query MBTA for predictions without an '
                                 'API key. Currently in `Anonymous` mode.')
        require_filters('stop', 'route', 'trip', **filters)
        predictions = self._engine.request(Prediction.list_route, **filters)
        return [Prediction(**prediction) for prediction in predictions]

    def facility(self, id):
        raise NotImplementedError

    def alert(self, id):
        raise NotImplementedError
