"""
Functions related to HTTP Basic Authorization

"""

from functools import wraps

from flask import request, Response, current_app


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
            assert request.authorization.username == \
                current_app.config['APP_USERNAME']
            assert request.authorization.password == \
                current_app.config['APP_PASSWORD']
        except AttributeError:
            return Response(
                'You must provide access credentials for this url.', 401,
                {'WWW-Authenticate': 'Basic'})
        except AssertionError:
            return Response(
                'Could not verify your access level for that URL.\n'
                'You have to login with proper credentials', 401,
                {'WWW-Authenticate': 'Basic'})

        return original_function(*args, **kwargs)
    return decorated