import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'mysql+pymysql://root:rootroot@localhost:3306/minifigs'
    SQLALCHEMY_TRACK_MODIFICATIONS = True