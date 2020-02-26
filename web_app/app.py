from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.tweet_routes import tweet_routes
from web_app.routes.admin_routes import admin_routes
from web_app.routes.ml_routes import ml_routes

import os
from dotenv import load_dotenv

load_dotenv()
DB_LOCATION = os.getenv('DB_LOCATION')

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{DB_LOCATION}'
    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(tweet_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(ml_routes)

    return app
