from functools import wraps


def relationship_id(f):
    """A quality of life decorator: returns f()['data']['id']

    Extracts the ID of a relationship field. Expects f to
    return a dict of { 'data': { 'id': foo } }. This wrapper will also
    catch any KeyError that has been raised (and will return None)
    """
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
            return result['data']['id']
        except KeyError:
            return None
    return wrapped
