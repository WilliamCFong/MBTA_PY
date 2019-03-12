class Queryable:
    """This superclass holds all common behaviors of a queryable route of
    MBTA's API v3"""

    @property
    def list_route(self):
        raise NotImplementedError

class SingularQueryable(Queryable):

    def __init__(self, id):
        self._id = id

    def __eq__(self, other):
        return self.id == other.id

    @property
    def id(self):
        return self._id

    @property
    def id_route(self):
        raise NotImplementedError

