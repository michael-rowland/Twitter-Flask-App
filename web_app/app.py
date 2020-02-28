from dotenv import load_dotenv
# from flask import Flask, jsonify, render_template, request
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from web_app.models import db, migrate
from web_app.routes.admin_routes import admin_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.ml_routes import ml_routes

load_dotenv()
DB_LOCATION = getenv('DB_LOCATION')

def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = 'super secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{DB_LOCATION}'
    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(ml_routes)

    return app
