from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from .models import Hero, Power, HeroPower
from .routes import register_routes
from flask_restful import Api
from app.resources.hero_resource import HeroListResource, HeroDetailResource
from app.resources.power_resource import PowerListResource, PowerDetailResource
from app.resources.hero_power_resource import HeroPowerListResource

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    register_routes(app)
    Migrate(app, db)

    api = Api(app)
    api.add_resource(HeroListResource, "/heroes")
    api.add_resource(HeroDetailResource, "/heroes/<int:id>")
    api.add_resource(PowerListResource, "/powers")
    api.add_resource(PowerDetailResource, "/powers/<int:id>")
    api.add_resource(HeroPowerListResource, "/hero_powers")

    return app
    

