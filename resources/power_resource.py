from flask_restful import Resource
from flask import request
from models import Power
from extensions import db

class PowerListResource(Resource):
    def get(self):
        powers = Power.query.all()
        return [power.to_dict() for power in powers], 200

class PowerDetailResource(Resource):
    def get(self, id):
        power = Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404
        return power.to_dict(), 200

    def patch(self, id):
        power = Power.query.get(id)
        if not power:
            return {"error": "Power not found"}, 404

        data = request.get_json()
        try:
            power.description = data.get("description")
            db.session.commit()
            return power.to_dict(), 200
        except Exception as e:
            return {"errors": [str(e)]}, 400
