from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions

from controllers import students


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/students', methods=['GET', 'POST'])
def students_handler():
    fns = {
        'GET': students.index,
        'POST': students.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/students/<int:student_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def student_handler(student_id):
    fns = {
        'GET': students.show,
        'PATCH': students.update,
        'PUT': students.update,
        'DELETE': students.destroy
    }
    resp, code = fns[request.method](request, student_id)
    return jsonify(resp), code

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

print("&&&&&&&&&&&&&&&&&", __name__)
