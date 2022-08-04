
class Config(object):
    DEBUG = True
    SECRET_HERE = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    JSON_AS_ASCII = False
    RESTX_JSON = False
    SQLALCHEMY_TRACK_MODIFICATIONS = {'ensure_ascii': False, 'indent': 3}

