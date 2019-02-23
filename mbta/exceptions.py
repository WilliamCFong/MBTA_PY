class MBTA_Exception(Exception):

    """Superclass for all Exceptions raised in mbta package. """

    pass

class MBTA_NotFound(MBTA_Exception):
    """ Raised when search returns 404 (Not Found). """

    def __init__(self, response, query_val):
        parameter = response['errors'][0]['source']['parameter']
        reason = response['errors'][0]['title']
        message = f'{parameter}: {query_val} {reason}'
        super().__init__(message)

class MBTA_Forbidden(MBTA_Exception):
    """ Raised when request returns a 403 HTTP error code. """

    def __init__(self, url):
        super().__init__(f'GET {url} returned 403 (Forbidden)')


class MBTA_QuotaExceeded(MBTA_Exception):
    """ Raised when user has made too many requests. """

    pass
