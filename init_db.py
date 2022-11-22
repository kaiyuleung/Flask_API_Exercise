from student import db
from student import app


with app.app_context():
    db.drop_all()
    db.create_all()
        
