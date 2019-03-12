from mbta.query_engine.query import SingularQueryable

class Trip(SingularQueryable):
    """ This class encompasses the data received from MBTA's Trip api"""

    id_route = 'trip'
    list_route = 'trips'

    def __init__(self, id, attributes, relationships):
        super().__init__(id)
        self._attributes = attributes
        self._relationships = relationships

    @property
    def bikes_allowed(self):
        return self._attributes['bikes_allowed']

    @property
    def block_id(self):
        return self._attributes['block_id']

    @property
    def direction_id(self):
        return self._attributes['direction_id']

    @property
    def headsign(self):
        return self._attributes['headsign']

    @property
    def name(self):
        return self._attributes['name']

    @property
    def wheelchair_accessible(self):
        return self._attributes['wheelchair_accessible']

    @property
    def route(self):
        try:
            return self._relationships['route']['data']['id']
        except KeyError:
            return None

    @property
    def service(self):
        try:
            return self._relationships['service']['data']['id']
        except KeyError:
            return None

    @property
    def shape(self):
        try:
            return self._relationships['shape']['data']['id']
        except KeyError:
            return None
