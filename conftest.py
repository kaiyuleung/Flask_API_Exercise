#! Not done with db
import pytest
import app
from controllers import students

@pytest.fixture
def api(monkeypatch):
    test_students = [
        {'id': 1, 'name': 'Tom', 'age': 100},
        {'id': 2, 'name': 'Emile', 'age': 150}
    ]
    monkeypatch.setattr(students, "students", test_students)
    api = app.app.test_client()
    return api
