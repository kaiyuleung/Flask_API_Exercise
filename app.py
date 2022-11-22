from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200
