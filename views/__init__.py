from flask import jsonify, session, request
from models.account import User, AnonymousUser


def method_not_allowed(err):
    return jsonify(code=405, msg=u'method not allowed')


def page_not_found(err):
    return jsonify(code=404, msg=u'page not found')


def get_user():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter_by(id=user_id, is_valid=True).first()
        if user:
            request.user = user
            return
    request.user = AnonymousUser()


def log():
    ip = request.remote_addr


def del_user(response):
    delattr(request, 'user')
    return response
