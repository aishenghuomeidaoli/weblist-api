# -*- coding: utf-8 -*-
from functools import wraps
from flask import jsonify, request


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.user.is_authenticated:
            return f(*args, **kwargs)
        return jsonify(code=405, msg=u'请登录')

    return decorated_function
