import unittest
from employee import Employee
from custom_exceptions import WrongPayRaisePercentError


# create a class that inherits from  unittest.TestCase
class TestEmployee(unittest.TestCase):

    def setUp(self):
        firstname = 'Bob'
        lastname = 'Ross'
        pay = 38000
        self.employee = Employee(firstname, lastname, pay)
        print("Setting up")

    def tearDown(self):
        print("Tear down!")

    def test_fullname_property(self):
        # arrange:
        expected_result = 'Bob Ross'
        # act:
        actual_result = self.employee.fullname
        # assert:
        self.assertEqual(actual_result, expected_result)

    def test_email_property(self):
        # arrange:
        expected_result = 'BobRoss@email.com'
        # act:
        actual_result = self.employee.email
        # assert:
        self.assertEqual(actual_result, expected_result)

    def test_raise_property(self):
        # arrange:
        expected_result = 3800
        # act:
        actual_result = self.employee.apply_raise(10)
        # assert:
        self.assertEqual(actual_result, expected_result)

    def test_too_big_pay_raise(self):
        self.assertRaises(WrongPayRaisePercentError, self.employee.apply_raise, 20)
