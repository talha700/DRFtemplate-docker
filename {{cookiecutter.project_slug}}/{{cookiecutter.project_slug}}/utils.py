
def remove_certain_endpoints(endpoints):
    """
    Preprocessing hook to exclude certain endpoints from OpenAPI schema
    :param endpoints:
    """
    return [
        (path, path_regex, method, callback) for path, path_regex, method, callback in endpoints
        if not (path.endswith('schema/'))
    ]
