from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# todo HOW DO I USE SQLITE HERE INSTEAD?
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(128))
    userid = db.Column(db.Integer)

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(128))
