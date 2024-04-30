from flask import Blueprint, request, jsonify
from models import db, Manufacturer, CarModel, Car

api_bp = Blueprint('api', __name__)

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return 'Vítejte v aplikaci pro správu automobilů!'

@api_bp.route('/manufacturers', methods=['GET', 'POST'])
def manufacturers():
    if request.method == 'GET':
        manufacturers = Manufacturer.query.all()
        return jsonify([manufacturer.serialize() for manufacturer in manufacturers])
    elif request.method == 'POST':
        data = request.json
        manufacturer = Manufacturer(name=data['name'], city=data['city'])
        db.session.add(manufacturer)
        db.session.commit()
        return jsonify(manufacturer.serialize()), 201

@api_bp.route('/models', methods=['GET', 'POST'])
def car_models():
    if request.method == 'GET':
        car_models = CarModel.query.all()
        return jsonify([car_model.serialize() for car_model in car_models])
    elif request.method == 'POST':
        data = request.json
        car_model = CarModel(name=data['name'], manufacturer_id=data['manufacturer_id'])
        db.session.add(car_model)
        db.session.commit()
        return jsonify(car_model.serialize()), 201

@api_bp.route('/cars', methods=['GET', 'POST'])
def cars():
    if request.method == 'GET':
        cars = Car.query.all()
        return jsonify([car.serialize() for car in cars])
    elif request.method == 'POST':
        data = request.json
        car = Car(model_id=data['model_id'], year=data['year'], color=data['color'])
        db.session.add(car)
        db.session.commit()
        return jsonify(car.serialize()), 201