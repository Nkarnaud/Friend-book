# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:16:09 2019

@author: nkeumo
"""


from functools import wraps

from flask import request, jsonify

from project.api.models import FriendBook


def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response_object = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify(response_object), 403
        auth_token = auth_header.split(" ")[1]
        resp = FriendBook.decode_auth_token(auth_token)
        if isinstance(resp, str):
            response_object['message'] = resp
            return jsonify(response_object), 401
        friend = FriendBook.query.filter_by(id=resp).first()
        if not friend or not friend.active:
            return jsonify(response_object), 401
        return f(resp, *args, **kwargs)
    return decorated_function
