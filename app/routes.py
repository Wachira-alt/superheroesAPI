from flask_restful import Api
from app.resources.hero_resource import HeroListResource, HeroDetailResource
from app.resources.power_resource import PowerListResource, PowerDetailResource
from app.resources.hero_power_resource import HeroPowerListResource

def register_routes(app):
    api = Api(app)

    api.add_resource(HeroListResource, "/heroes")
    api.add_resource(HeroDetailResource, "/heroes/<int:id>")

    api.add_resource(PowerListResource, "/powers")
    api.add_resource(PowerDetailResource, "/powers/<int:id>")

    api.add_resource(HeroPowerListResource, "/hero_powers")
