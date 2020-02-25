
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.String(128))

# todo HOW DO I USE SQLITE HERE INSTEAD?
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    tweet = db.Column(db.String(128))

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(128))
