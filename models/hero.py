from extensions import db
from sqlalchemy_serializer import SerializerMixin

class Hero(db.Model, SerializerMixin):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    hero_powers = db.relationship("HeroPower", backref="hero", cascade="all, delete-orphan")

    # Avoid circular references in nested serialization
    serialize_rules = ("-hero_powers.hero",)
