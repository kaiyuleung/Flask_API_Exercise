from flask import Blueprint, request, jsonify
from werkzeug import exceptions

# from ..controllers import students
from ..models.student import Student

from ..database.db import db

main_routes = Blueprint("main", __name__)

@main_routes.route('/api/students', methods=['GET', 'POST'])
def students_handler():
    if request.method == 'GET':
        students = Student.query.all()
        output = map(lambda p: { 
            "id": p.id,
            "name": p.name, 
            "age": p.age
            }, students)
        usable_output = list(output)
        return jsonify(usable_output), 200
    elif request.method == 'POST':
        sData = request.json
        new_student = Student(
            name = sData['name'],
            age = sData['age']
            )
        db.session.add(new_student)
        db.session.commit()
        return jsonify(sData), 201
    
@main_routes.route('/api/students/<int:student_id>', methods=['GET', 'DELETE'])
def student_handler(student_id):
    if request.method == 'GET':
        try: 
            foundStudent = Student.query.filter_by(id=int(student_id)).first()
            output = {"name": foundStudent.name, "age": foundStudent.age}
            return output
        except:
            raise exceptions.BadRequest(f"We do not have a pokemon with that id: {student_id}")
    if request.method == 'DELETE':
        try: 
            foundStudent = Student.query.filter_by(id=int(student_id)).first()
            db.session.delete(foundStudent)
            db.session.commit()
            return "deleted", 204
        except:
            raise exceptions.BadRequest(f"We do not have a pokemon with that id: {student_id}")




# @main_routes.route('/api/students', methods=['GET', 'POST'])
# def students_handler():
#     fns = {
#         'GET': students.index,
#         'POST': students.create
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
