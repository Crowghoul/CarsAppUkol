from flask_restful import Resource, reqparse
from models import db, Manufacturer, CarModel, Car

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name of the car manufacturer')
parser.add_argument('city', type=str, help='City where the manufacturer is located')
parser.add_argument('model_name', type=str, help='Name of the car model')
parser.add_argument('year', type=int, help='Year of the car')
parser.add_argument('color', type=str, help='Color of the car')

class ManufacturerResource(Resource):
    def get(self, manufacturer_id):
        manufacturer = Manufacturer.query.get(manufacturer_id)
        if manufacturer:
            return {'id': manufacturer.id, 'name': manufacturer.name, 'city': manufacturer.city}
        else:
            return {'message': 'Manufacturer not found'}, 404

    def post(self):
        args = parser.parse_args()
        manufacturer = Manufacturer(name=args['name'], city=args['city'])
        db.session.add(manufacturer)
        db.session.commit()
        return {'id': manufacturer.id, 'name': manufacturer.name, 'city': manufacturer.city}, 201

class CarModelResource(Resource):
    def get(self, model_id):
        car_model = CarModel.query.get(model_id)
        if car_model:
            return {'id': car_model.id, 'name': car_model.name, 'manufacturer_id': car_model.manufacturer_id}
        else:
            return {'message': 'Car model not found'}, 404

    def post(self):
        args = parser.parse_args()
        car_model = CarModel(name=args['model_name'], manufacturer_id=args['manufacturer_id'])
        db.session.add(car_model)
        db.session.commit()
        return {'id': car_model.id, 'name': car_model.name, 'manufacturer_id': car_model.manufacturer_id}, 201

class CarResource(Resource):
    def get(self, car_id):
        car = Car.query.get(car_id)
        if car:
            return {'id': car.id, 'model_id': car.model_id, 'year': car.year, 'color': car.color}
        else:
            return {'message': 'Car not found'}, 404

    def post(self):
        args = parser.parse_args()
        car = Car(model_id=args['model_id'], year=args['year'], color=args['color'])
        db.session.add(car)
        db.session.commit()
        return {'id': car.id, 'model_id': car.model_id, 'year': car.year, 'color': car.color}, 201