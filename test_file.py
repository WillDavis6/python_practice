from assert_file import adder
from unittest import TestCase

class AdditionTestCase(TestCase):
    """ examples of unittest case"""

    def test_adder(self):

        self.assertEqual(adder(2, 2), 4)



