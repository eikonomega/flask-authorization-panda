"""
Functions related to HTTP Basic Authorization

"""

from functools import wraps

from flask import request, jsonify, current_app


def basic_auth(original_function):
    """
    Wrapper.  Verify that request.authorization exists and that its
    contents match the application's config.basic_auth_credentials
    dict.

    Args:
        original_function (function): The function to wrap.

    Returns:
        flask.Response: When credentials are missing or don't match.
        original_function (function): The original function.

    """

    @wraps(original_function)
    def decorated(*args, **kwargs):
        try:
            if not (request.authorization.username,
                    request.authorization.password) == (
                    current_app.config.basic_auth_credentials['username'],
                    current_app.config.basic_auth_credentials['password']):
                unauthorized_response = jsonify(
                    {'message': 'Could not verify your access level '
                                'for that URL. \nYou have to login '
                                'with proper credentials',
                     'statusCode': 401})
                unauthorized_response.status_code = 401
                return unauthorized_response
        except AttributeError:
            unauthorized_response = jsonify(
                {'message': 'Could not verify your access level '
                            'for that URL. \nYou have to login '
                            'with proper credentials',
                 'statusCode': 401})
            unauthorized_response.status_code = 401

        return original_function(*args, **kwargs)
    return decorated