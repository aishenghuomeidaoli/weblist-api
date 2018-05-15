# -*- coding: utf-8 -*-
import datetime
import uuid
import hashlib

from flask import current_app

from weblist import db


class AnonymousUser(object):
    id = None

    @property
    def is_authenticated(self):
        return False


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid1)

    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(40), nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

    is_valid = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password):
        hash_md5 = hashlib.md5(password + current_app.config['SECRET_KEY'])
        return hash_md5.hexdigest()

    def check_password(self, password):
        return self._hash_password(password) == self.password_hash

    @property
    def is_authenticated(self):
        return True

    def __repr__(self):
        return '<User %r>' % self.username
