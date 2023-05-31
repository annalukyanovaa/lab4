import unittest
import requests
from app import app


class TestHTMLPage(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_page(self):
        response=requests.get('http://127.0.0.1:5000')
        self.assertEqual(response.status_code,200)

    def test_solution1(self):
        response = self.app.post('/', data=dict(a=1, b=-5, c=6))
        self.assertTrue(f'Квадратное уравнение имеет два корня: x1=2.0 и x2=3.0',  response.data)

    def test_solution2(self):
        response = self.app.post('/', data=dict(a=1, b=-4, c=4))
        self.assertTrue(f'Квадратное уравнение имеет один корень: x=2.0',  response.data)

    def test_solution3(self):
        response = self.app.post('/', data=dict(a=1, b=1, c=1))
        self.assertTrue(f'Квадратное уравнение не имеет действительных корней',  response.data)

if __name__ == '__main__':
    unittest.main()