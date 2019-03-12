from mbta.query_engine.query import SingularQueryable


class Route(SingularQueryable):
    """This class represents an MBTA Route."""

    route = 'route'
    list_routes = 'routes'

    def __init__(self, id, attributes, relationships):
        super().__init__(id)
        self._attributes = attributes
        self._relationships = relationships

    def __repr__(self):
        return f'<Route {self.short_name}: {self.long_name} [{self.description}]>'

    @property
    def color(self):
        return self._attributes['color']

    @property
    def text_color(self):
        return self._attributes['text_color']

    @property
    def description(self):
        return self._attributes['description']

    @property
    def destinations(self):
        return (
            self._attributes['direction_destinations'][0],
            self._attributes['direction_destinations'][1]
        )

    @property
    def directions(self):
        return (
            self._attributes['direction_names'][0],
            self._attributes['direction_names'][1]
        )

    @property
    def fare_class(self):
        return self._attributes['fare_class']

    @property
    def long_name(self):
        return self._attributes['long_name']

    @property
    def short_name(self):
        return self._attributes['short_name']

    @property
    def route_type(self):
        return self._attributes['type']

    @property
    def line(self):
        """Returns the id of the line related to the route"""
        return self._relationships['line']['data']['id']
