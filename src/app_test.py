from app import app

import unittest
import json

class CitiesTestCase(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/cities.json', content_type='application/json')
    print(response.status_code)
    print(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(json.loads(response.data), ['Amsterdam', 'San Francisco', 'Berlin', 'New York'])

if __name__ == '__main__':
    unittest.main()
