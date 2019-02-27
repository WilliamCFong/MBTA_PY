class Stop:

    """Encompasses a stop in an MBTA Line."""

    def __init__(self, id, attributes):
        self.id = id
        self._attributes = attributes
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
