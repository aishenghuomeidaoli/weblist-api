import os
from datetime import timedelta


class ConfigBase:
    """config base class"""
    HOST = '127.0.0.1'
    PORT = 5000
    SECRET_KEY = 'secret-key'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigDev(ConfigBase):
    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)

    SQLALCHEMY_DATABASE_URI = \
        'mysql://root:zhujiawei@localhost/weblist?charset=utf8'
    SESSION_REFRESH_EACH_REQUEST = True


class ConfigPro(ConfigBase):
    # session config
    SESSION_COOKIE_DOMAIN = '.weblist.site'
    SESSION_COOKIE_PATH = '/'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # change secret key if set in environ
    SECRET_KEY = os.environ.get('WEBLIST_SECRET_KEY') or ConfigBase.SECRET_KEY

    SQLALCHEMY_DATABASE_URI = os.environ.get('WEBLIST_SQLALCHEMY_DATABASE_URI')
    SESSION_REFRESH_EACH_REQUEST = True
