from dateutil.parser import parse
from mbta.query_engine.query import SingularQueryable

class Schedule(SingularQueryable):

    """ This class encompasses a single Schedule stop."""
    route = 'schedule'

    def __init__(self, id, attributes, relationships=None):
        super().__init__(id)
        self._attributes = attributes
        self._relationships = relationships

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
