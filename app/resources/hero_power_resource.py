from flask_restful import Resource
from flask import request
from app.models import HeroPower, Hero
from app.extensions import db

class HeroPowerListResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_hp = HeroPower(
                strength=data["strength"],
                hero_id=data["hero_id"],
                power_id=data["power_id"]
            )
            db.session.add(new_hp)
            db.session.commit()

            hero = Hero.query.get(data["hero_id"])

            return hero.to_dict(), 201
        except Exception as e:
            return {"errors": [str(e)]}, 400
