from flask import session
from config import db

class City_cfg(db.Model):
    __tablename__ = 'cities_cfg'
    id = db.Column(db.Integer, primary_key=True)
    city_a = db.Column(db.Integer)
    city_b = db.Column(db.Integer)
    city_c = db.Column(db.Integer)

    