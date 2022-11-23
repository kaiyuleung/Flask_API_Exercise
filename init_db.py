# from student import db
# from student import app


# with app.app_context():
#     db.drop_all()
#     db.create_all()

from student import db
from student import app
from student.models.student import Student

students = [
    { 'name': 'Oliver', 'age': 24},
    { 'name': 'Matthieu', 'age': 26},
    { 'name': 'Kai', 'age': 26}
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for student in students:
        db.session.add(Student(name = student['name'], age = student['age']))
    db.session.commit()




