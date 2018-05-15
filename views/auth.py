# -*- coding: utf-8 -*-
from flask import jsonify, request, session, Blueprint

from models.account import User, AnonymousUser
from utils.decorators import login_required
from weblist import db

auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.route('/register/', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    password_repeat = request.form.get('password_repeat')
    if not user or not password or not password_repeat:
        return jsonify(code=101, msg=u'参数不全')
    if password_repeat != password:
        return jsonify(code=101, msg=u'密码不一致')
    row = User(username=username)
    row.set_password(password)
    db.session.add(row)
    db.session.commit()
    return jsonify(code=200, msg=u'注册成功')


@auth.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return jsonify(code=101, msg=u'参数不全')
    row = User.query.filter_by(username=username, is_valid=True).first()
    if not row:
        return jsonify(code=102, msg=u'用户不存在')
    if not row.check_password(password):
        return jsonify(code=101, msg=u'密码错误')
    session['user_id'] = row.id
    return jsonify(code=200, msg=u'登录成功')


@auth.route('/logout/')
def logout():
    session.clear()
    return jsonify(code=200, msg=u'退出成功')


@auth.route('/user/')
@login_required
def user():
    return jsonify(
        code=200,
        data=dict(id=request.user.id,
                  username=request.user.username))
