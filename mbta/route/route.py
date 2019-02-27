class Route:
    """This class represents an MBTA Route."""

    def __init__(self, id, attributes):
        self._attributes = attributes
        self.id = id

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
    def direction(self):
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
