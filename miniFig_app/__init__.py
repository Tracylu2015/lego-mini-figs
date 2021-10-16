from flask import Flask
from miniFig_app.config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
db.init_app(app)

# Create migration script
migrate = Migrate(app, db)

from miniFig_app.models.figure import Figure # import model class so it can be initalized
from miniFig_app.models.user import User # import model class so it can be initalized

# Create database table
with app.app_context():
    db.create_all()