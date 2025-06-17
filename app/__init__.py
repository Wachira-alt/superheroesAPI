from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from .models import Hero, Power, HeroPower
from .routes import register_routes

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    register_routes(app)
    Migrate(app, db)

    return app
    

