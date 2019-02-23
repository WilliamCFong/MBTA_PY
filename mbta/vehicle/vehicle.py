class Vehicle:

    """This class encompasses the data sent and received from MBTA's vehicle
    API subdomain."""

    def __init__(self, id, trip=False, stop=False, route=False):
        """Search for and return a Vehicle

        :id: The ID of the vehicle to obtain.
        :trip: TODO
        :stop: TODO
        :route: TODO

        """
        self._id = id
        self._trip = trip
        self._stop = stop
        self._route = route
        raise NotImplementedError
