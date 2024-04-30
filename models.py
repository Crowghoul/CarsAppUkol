from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

class CarModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=False)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('car_model.id'), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)