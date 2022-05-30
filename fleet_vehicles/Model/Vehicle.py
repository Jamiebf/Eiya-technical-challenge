from config import db, relationship, backref
from Model.City import City

class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    cities_id = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)
    city = relationship(City, backref = backref('vehicles'))
    consume = db.Column(db.Float)
    distance = db.Column(db.Integer)
    consumed = db.Column(db.Float)
