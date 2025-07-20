import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_trace_endpoint(self):
        sql_script = "SELECT id, name, value AS amount INTO new_table FROM old_table;"
        response = self.app.post('/trace', data={'sql_script': sql_script})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['tabla_fuente'], 'old_table')

if __name__ == '__main__':
    unittest.main()
