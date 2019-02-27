def get_lines(page_offset=0, page_limit=10, sort=None, include_routes=True):
    """Returns a list of MBTA Lines based upon the search parameters given."""
    raise NotImplementedError

class Line:
    """This class represents MBTA Lines."""

    def __init__(self, id, attributes):
        self.id = id
        self.attributes = attributes

    @property
    def color(self):
        return self.attributes['color']

    @property
    def text_color(self):
        return self.attributes['text_color']

    @property
    def long_name(self):
        return self.attributes['long_name']

    @property
    def short_name(self):
        return self.attributes['short_name']

