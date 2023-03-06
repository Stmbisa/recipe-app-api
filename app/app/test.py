"""
sample test
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """ test the calc function"""
    def test_add_numbers(self):
        """ test adding the numbers """
        res = calc.add(5,6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ test subtracting the numbers """
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
