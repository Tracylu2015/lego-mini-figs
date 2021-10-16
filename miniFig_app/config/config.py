import os
basedir = os.path.abspath(os.path.dirname(__file__))

print(os.getenv('DATABASE_URL'))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False