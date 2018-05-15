# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(getattr(config, config_name))

    db.init_app(app)

    from views import method_not_allowed, page_not_found, get_user, log, \
        del_user
    app.errorhandler(404)(page_not_found)
    app.errorhandler(405)(method_not_allowed)

    app.before_request(get_user)
    app.before_request(log)
    app.after_request(del_user)

    from views.auth import auth
    app.register_blueprint(auth)

    return app
