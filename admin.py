from flask import abort
from functools import wraps
from flask_login import current_user


def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        return function(*args, **kwargs) if current_user.id == 1 else abort(403)

    return decorated_function
