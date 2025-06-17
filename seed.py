# seed.py
from app import create_app
from app.extensions import db
from app.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    print("Resetting DB...")
    db.drop_all()
    db.create_all()

    print("Seeding Heroes...")
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra"),
    ]
    db.session.add_all(heroes)

    print("Seeding Powers...")
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths"),
    ]
    db.session.add_all(powers)

    db.session.commit()

    print("Done seeding!")
