from flask import jsonify
from werkzeug.exceptions import BadRequest

from ..models.student import Student
from ..database.db import db

class Format():
    ''' ASCI codes for formatting '''
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CLEAR = '\033[0m'

def index(req):
    print(f"\n{Format.GREEN}{Format.BOLD}students.index() {Format.CLEAR}")
    
    #* Class instance
    students = Student.query.all()
    print(f"{Format.BLUE}{Format.BOLD}Student.query.all() {Format.CLEAR}\n", students)
    
    #* Map instance
    output = map(lambda p: { 
        "id": p.id,
        "name": p.name, 
        "age": p.age
        }, students)
    print(f"{Format.BLUE}{Format.BOLD}map(lambda p: ... {Format.CLEAR}\n", output)
    
    #* List instance
    usable_output = list(output)
    print(f"{Format.BLUE}{Format.BOLD}list() {Format.CLEAR}\n", usable_output)
    
    #* JSON-Response instance
    print(f"{Format.BLUE}{Format.BOLD}jsonify() {Format.CLEAR}\n", jsonify(usable_output))
    return usable_output, 200

def show(req, uid):
    print(f"\n{Format.GREEN}{Format.BOLD}students.show() {Format.CLEAR}")
    
    foundStudent = find_by_uid(uid)
    #* Dictionary instance
    output = {"name": foundStudent.name, "age": foundStudent.age}
    print(f'{Format.BLUE}{Format.BOLD} {Format.CLEAR}\n', output)
    
    #* JSON-Response instance
    print(f'{Format.BLUE}{Format.BOLD}jsonify(sData) {Format.CLEAR}\n', jsonify(output))
    return output, 200

def create(req):
    print(f"\n{Format.GREEN}{Format.BOLD}students.create() {Format.CLEAR}")
    
    sData = req.json
    #* JSON-Request instance
    print(f'{Format.BLUE}{Format.BOLD}request {Format.CLEAR}\n', req)
    #* JSON instance
    print(f'{Format.BLUE}{Format.BOLD}request.json {Format.CLEAR}\n', sData)

    # No need to convert to a Map instance as there is only one item
    #* Class instance    
    new_student = Student(
        name = sData['name'],
        age = sData['age']
        )
    print(f'{Format.BLUE}{Format.BOLD}Student(...sData){ Format.CLEAR}\n', new_student)
    
    db.session.add(new_student)
    db.session.commit()
    
    #* JSON-Response instance
    print(f'{Format.BLUE}{Format.BOLD}jsonify(sData) {Format.CLEAR}\n', jsonify(sData))
    return sData, 201

def update(req, uid):
    print(f"\n{Format.GREEN}{Format.BOLD}students.update() {Format.CLEAR}")#
    
    foundStudent = find_by_uid(uid)
    if req.json.get('name') != None:
        foundStudent.name = req.json['name']
    if req.json.get('age') != None:
        foundStudent.age = req.json['age']
    db.session.commit()
    
    resp, code = show(req, uid)
    return resp, 200

def destroy(req, uid):
    print(f"\n{Format.GREEN}{Format.BOLD}students.destroy() {Format.CLEAR}")

    foundStudent = find_by_uid(uid)
    db.session.delete(foundStudent)
    db.session.commit()
    return { "message" : "deleted" }, 204


def find_by_uid(uid):
    print(f"\n{Format.GREEN}{Format.BOLD}students.find_by_uid() {Format.CLEAR}")
    try:
        #* Class instance
        foundStudent = Student.query.filter_by(id = int(uid)).first()
        print(f'{Format.BLUE}{Format.BOLD}Student.query... {Format.CLEAR}\n', foundStudent)

        return foundStudent
    except:
        raise BadRequest(f"We don't have that student with id {uid}!")
