from flask_restful import Resource
from flask import request
from models import Hero
from extensions import db

class HeroListResource(Resource):
    def get(self):
        heroes = Hero.query.all()
        return [hero.to_dict() for hero in heroes], 200

class HeroDetailResource(Resource):
    def get(self, id):
        hero = Hero.query.get(id)
        if not hero:
            return {"error": "Hero not found"}, 404
        return hero.to_dict(), 200
