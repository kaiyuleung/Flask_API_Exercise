from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest

from ..models.student import Student

# students = [
#     {'id': 1, 'name': 'Oliver', 'age': 24},
#     {'id': 2, 'name': 'Matthieu', 'age': 26},
#     {'id': 3, 'name': 'Kai', 'age': 26}
# ]

def index(req):
    students = Student.query.all()
    output = map(lambda p: { 
        "name": p.name, 
        "age": p.age
        }, students)
    return jsonify(list(output)), 200
    # return [s for s in students], 200

# def show(req, uid):
#     return find_by_uid(uid), 200

# def create(req):
#     # new_student = req.get_json()
#     new_student = req.json
#     new_student['id'] = sorted([s['id'] for s in students])[-1] + 1
#     students.append(new_student)
#     return new_student, 201

# def update(req, uid):
#     student = find_by_uid(uid)
#     data = req.get_json()
#     print(data)
#     for key, val in data.items():
#         student[key] = val
#     return student, 200

# def destroy(req, uid):
#     student = find_by_uid(uid)
#     students.remove(student)
#     return student, 204

# def find_by_uid(uid):
#     try:
#         return next(student for student in students if student['id'] == uid)
#     except:
#         raise BadRequest(f"We don't have that student with id {uid}!")
