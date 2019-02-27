from dateutil.parser import parse

class Vehicle:

    """This class encompasses the data sent and received from MBTA's vehicle
    API subdomain."""

    def __init__(self, id, attributes, relationships):
        """Initializes a Vehicle"""
        self.id = id
        self._attributes = attributes
        self._relationships = relationships

    @property
    def bearing(self):
        """Returns the bearing of the Vehicle"""
        return self._attributes['bearing']

    @property
    def status(self):
        """Returns the current status of the Vehicle"""
        return self._attributes['current_status']

    @property
    def stop_sequence(self):
        """Returns the current stop sequence of the Vehicle"""
        return self._attributes['current_stop_sequence']

    @property
    def direction_id(self):
        """Returns the current direction ID of the Vehicle"""
        return self._attributes['direction_id']

    @property
    def latitude(self):
        """Returns the latitude of the Vehicle"""
        return self._attributes['latitude']

    @property
    def longitude(self):
        """Returns the longitude of the Vehicle"""
        return self._attributes['longitude']

    @property
    def speed(self):
        """Returns the speed of the Vehicle"""
        return self._attributes['speed']

    @property
    def updated_at(self):
        """The timestamp of the latest information sample for the Vehicle"""
        return parse(self._attributes['updated_at'])

    @property
    def route(self):
        """Returns the id of the route the Vehicle is currently on"""
        return self._relationships['route']['data']['id']

    @property
    def stop(self):
        """Returns the id of the stop the Vehicle is currently on"""
        return self._relationships['stop']['data']['id']

    @property
    def trip(self):
        """Returns the id of the trip the Vehicle is currently on"""
        return self._relationships['trip']['data']['id']
