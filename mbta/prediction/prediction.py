from dateutil.parser import parse
from mbta.query_engine.query import Queryable
from mbta.query_engine.decorators import relationship_id

class Prediction(Queryable):

    """An MBTA Prediction response."""

    list_route = 'predictions'

    def __init__(self, id, attributes, relationships):
        super().__init__()
        self._id = id
        self._attributes = attributes
        self._relationships = relationships

    @property
    def id(self):
        return self._id

    @property
    def stop_sequence(self):
        """The stop sequence of the Prediction. This value increases
        monotonically within a trip. But that difference is not necessarily
        1.
        """
        return self._attributes['stop_sequence']

    @property
    def status(self):
        """The status of the schedule."""
        return self._attributes['status']

    @property
    def schedule_relationship(self):
        """A string describing how the predicted stop relates to a schedule.

        For more information see the GTFS section on ScheduleRelationship

        Returns:
            str: The schedule relationship.

        Examples:
            >>> p.schedule_relationship
            'SKIPPED'
        """
        return self._attributes['schedule_relationships']

    @property
    def direction_id(self):
        """The direction of the current trip within this prediction.
        Returns:
            int: The index of the direction name array for the current
            trip.
        """
        return self._attributes['direction_id']

    @property
    def departure_time(self):
        """When the current vehicle is expected to depart. Returns None
        if this is the last stop.
        Returns:
            datetime: The depature time, parsed from an ISO8601 string.
        """
        try:
            return parse(self._attributes['departure_time'])
        except TypeError:
            return None

    @property
    def arrival_time(self):
        """WHen the current vehicle is expected to arrive. Returns None
        if this is the first stop.
        Returns:
            datetime: The arrival time, parsed from an ISO8601 string.
        """
        try:
            return parse(self._attributes['arrival_time'])
        except TypeError:
            return None

    @property
    @relationship_id
    def vehicle(self):
        return self._relationships['vehicle']

    @property
    @relationship_id
    def trip(self):
        return self._relationships['trip']

    @property
    @relationship_id
    def stop(self):
        return self._relationships['stop']

    @property
    @relationship_id
    def schedule(self):
        return self._relationships['schedule']

    @property
    @relationship_id
    def alert(self):
        return self._relationships['alert']
