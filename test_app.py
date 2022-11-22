import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from Flask!'

    def test_get_students(self, api):
        res = api.get('/api/students')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_get_student(self, api):
        res = api.get('/api/students/2')
        assert res.status == '200 OK'
        assert res.json['name'] == 'Emile'

    def test_get_students_error(self, api):
        res = api.get('/api/students/4')
        assert res.status == '400 BAD REQUEST' and "student with id 4" in res.json['message']
        # assert "We don't have that student with id 4" in res.json['message']

    def test_post_students(self, api):
        mock_data = json.dumps({'name': 'Ree'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/students', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 3

    def test_patch_student(self, api):
        mock_data = json.dumps({'name': 'Ree'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.patch('/api/students/2', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 2
        assert res.json['name'] == 'Ree'

    def test_delete_student(self, api):
        res = api.delete('/api/students/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/bob')
        assert res.status == '404 NOT FOUND' and 'Oops!' in res.json['message']
        # assert 'Oops! 404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.' in res.json['message']

    # def test_Internal_Server_Error(self, api):
    #     res = api.get('/bob')
    #     assert res.status == '404 NOT FOUND' and 'Oops!' in res.json['message']
