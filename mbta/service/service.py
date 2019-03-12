from dateutil.parser import parse
from mbta.query_engine.query import SingularQueryable

class Service(SingularQueryable):

    """This class encompases the data received from MBTA's Service API hook"""

    id_route = 'service'
    list_route = 'vehicles'

    def __init__(self, id, attributes):
        super().__init__(id)
        self._attributes = attributes

    @property
    def added_dates(self):
        return [parse(x) for x in self._attributes['added_dates']]

    @property
    def notes(self):
        return self._attributes['added_dates_notes']

    @property
    def description(self):
        return self._attributes['description']

    @property
    def start_date(self):
        return parse(self._attributes['start_date'])

    @property
    def end_date(self):
        return parse(self._attributes['end_date'])

    @property
    def removed_dates(self):
        return [parse(x) for x in self._attributes['removed_dates']]

    @property
    def removed_dates_notes(self):
        return self._attributes['removed_dates_notes']

    @property
    def schedule_name(self):
        return self._attributes['schedule_name']

    @property
    def schedule_type(self):
        return self._attributes['schedule_type']

    @property
    def schedule_typicality(self):
        return self._attributes['schedule_typicality']

    @property
    def valid_days(self):
        return self._attributes['valid_days']
