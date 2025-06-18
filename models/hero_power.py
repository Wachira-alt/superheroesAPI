from extensions import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"), nullable=False)

    @validates("strength")
    def validate_strength(self, key, value):
        valid_strengths = ["Strong", "Weak", "Average"]
        if value not in valid_strengths:
            raise ValueError(f"Strength must be one of {valid_strengths}")
        return value

    serialize_rules = ("-hero.hero_powers",)
