
class Config(object):
    DEBUG = True
    SECRET_HERE = '123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 3}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

