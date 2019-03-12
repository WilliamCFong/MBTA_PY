from mbta.query_engine.query import SingularQueryable

def get_lines(page_offset=0, page_limit=10, sort=None, include_routes=True):
    """Returns a list of MBTA Lines based upon the search parameters given."""
    raise NotImplementedError

class Line(SingularQueryable):
    """This class represents MBTA Lines."""

    id_route = 'line'
    list_route = 'lines'

    def __init__(self, id, attributes):
        super().__init__(id)
        self._attributes = attributes

    @property
    def color(self):
        return self._attributes['color']

    @property
    def text_color(self):
        return self._attributes['text_color']

    @property
    def long_name(self):
        return self._attributes['long_name']

    @property
    def short_name(self):
        return self._attributes['short_name']

    @property
    def sort_order(self):
        return self._attributes['sort_order']
