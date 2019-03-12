from mbta.query_engine.query import SingularQueryable

class Stop(SingularQueryable):

    """Encompasses a stop in an MBTA Line."""

    id_route = 'stop'
    list_route = 'stops'

    def __init__(self, id, attributes, relationships):
        super().__init__(id)
        self._attributes = attributes
        self._relationships = relationships
        self._schedule = None

    @property
    def address(self):
        return self._attributes['address']

    @property
    def description(self):
        return self._attributes['description']

    @property
    def latitude(self):
        return self._attributes['latitude']

    @property
    def longitude(self):
        return self._attributes['longitude']

    @property
    def location_type(self):
        return self._attributes['location_type']

    @property
    def name(self):
        return self._attributes['name']

    @property
    def platform_code(self):
        return self._attributes['platform_code']

    @property
    def platform_name(self):
        return self._attributes['platform_name']

    @property
    def accessibility(self):
        return self._attributes['wheelchair_boarding']

    # Begin Relationship properties
    @property
    def child_stops(self):
        """Returns a list of child stop ids."""
        return [x['id'] for x in self._relationships['child_stops']['data']]

    @property
    def parent_station(self):
        """Returns the parent station to this stop."""
        return self._relationships['parent_station']['data']
