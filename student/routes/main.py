from flask import Blueprint, request, jsonify

# from ..controllers.students import students
from ..models.student import Student

from ..database.db import db
# from ..models.student import Student

main_routes = Blueprint("main", __name__)

@main_routes.route('/api/students', methods=['GET'])
def Students_handler():
    if request.method == 'GET':
        students = Student.query.all()
        output = map(lambda p: { 
            "name": p.name, 
            "age": p.age
            }, students)
        return jsonify(list(output)), 200





# @main_routes.route('/api/students', methods=['GET', 'POST'])
# @main_routes.route('/api/students', methods=['GET'])
# def students_handler():
#     fns = {
#         'GET': students.index,
#         # 'POST': students.create
#     }
#     resp, code = fns[request.method](request)
#     return jsonify(resp), code

# @main_routes.route('/api/students/<int:student_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
# def student_handler(student_id):
#     fns = {
#         'GET': students.show,
#         'PATCH': students.update,
#         'PUT': students.update,
#         'DELETE': students.destroy
#     }
#     resp, code = fns[request.method](request, student_id)
#     return jsonify(resp), code
