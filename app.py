from flask import Flask
from extensions import db, migrate
from flask_restful import Api
from config import Config
from models import Hero, Power, HeroPower
from resources.hero_resource import HeroListResource, HeroDetailResource
from resources.power_resource import PowerListResource, PowerDetailResource
from resources.hero_power_resource import HeroPowerListResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

   

    db.init_app(app)
    migrate.init_app(app, db)

    api = Api(app)
    api.add_resource(HeroListResource, "/heroes")
    api.add_resource(HeroDetailResource, "/heroes/<int:id>")
    api.add_resource(PowerListResource, "/powers")
    api.add_resource(PowerDetailResource, "/powers/<int:id>")
    api.add_resource(HeroPowerListResource, "/hero_powers")

    return app

app = create_app()
    

