from assert_file import adder
from unittest import TestCase

from app import app

debug

class AdditionTestCase(TestCase):
    """ examples of unittest case"""

    def test_adder(self):

        self.assertEqual(adder(2, 2), 4)
        self.assertRaises(ValueError, adder, "f", "k")


class ColorViewsTestCase(TestCase):
    def test_color_form(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 400)
            self.assertIn('<h1>Color Form </h1>', html)

    def test_color_form(self):
        with app.test_client() as client:
            res = client.post('/fav-color', data= {'color': 'blue'})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 400)
            self

    def test_submit_taxes(self):
        with app.test_client as client:
            res = client.post('/taxes', data={'income': '1000'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3>You owe $150</h3>', html)
    def test_calc_taxes(self):
        self.assertEqual(calc_taxes(100), 15)
