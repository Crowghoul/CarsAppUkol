from flask import Blueprint

from flask import Flask
from routes import api_bp, home_bp
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(api_bp)
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)