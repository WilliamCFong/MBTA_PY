from dateutil.parser import parse
from mbta.query_engine.query import Queryable

class Schedule(Queryable):

    """ This class encompasses a single Schedule stop."""
    list_route = 'schedules'

    def __init__(self, id, attributes, relationships=None):
        self._id = id  # Schedules have an ID but do not have a /schedule/{id} route
        self._attributes = attributes
        self._relationships = relationships

    @property
    def id(self):
        return self._id

    @property
    def arrival_time(self):
        """Returns the expected arrival time as a datetime object"""
        return parse(self._attributes['arrival_time'])

    @property
    def departure_time(self):
        """Returns the expected departure time as a datetime object"""
        return parse(self._attributes['departure_time'])

    @property
    def drop_off_type(self):
        return self._attributes['drop_off_type']

    @property
    def pickup_type(self):
        return self._attributes['pickup_type']

    @property
    def stop_sequence(self):
        return self._attributes['stop_sequence']

    @property
    def timepoint(self):
        return self._attributes['timepoint']

    @property
    def prediction(self):
        raise NotImplementedError  #Check to see how predictions are handled for schedules

    @property
    def route(self):
        return self._relationships['route']['data']['id']

    @property
    def stop(self):
        return self._relationships['stop']['data']['id']

    @property
    def trip(self):
        return self._relationships['trip']['data']['id']
