from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug import exceptions

#* Router
from .routes.main import main_routes

#* Database
from dotenv import load_dotenv
from os import environ
from .database.db import db

load_dotenv()
database_uri = environ.get('DATABASE_URL')

#* API
app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI = database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)
CORS(app)
with app.app_context():
    db.app = app
    db.init_app(app)
    
    

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

app.register_blueprint(main_routes)



@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
