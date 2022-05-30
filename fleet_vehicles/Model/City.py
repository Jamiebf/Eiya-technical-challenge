from config import db, relationship, backref
from Model.City_cfg import City_cfg

class City(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    configuration_id = db.Column(db.Integer, db.ForeignKey('cities_cfg.id'), nullable=False)
    city_cfg = relationship(City_cfg, backref = backref('cities'))
    

    