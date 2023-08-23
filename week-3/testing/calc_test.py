# unit testing with unittests
# pytest - maybe for the future

import unittest

import calc


# create a class that inherits from  unittest.TestCase
class TestCalc(unittest.TestCase):

    def test_add(self):
        # Triple 'A' pattern
        # Arrange.....Act.....Assert
        # Given.......When......Then

        # arrange:
        number1 = 10
        number2 = 3
        expected_result = 13

        # act:
        actual_result = calc.add(number1, number2)

        # assert:
        self.assertEqual(actual_result, expected_result)

    def test_two_positive_ints_return_positive_int(self):
        # arrange:
        number1 = 2
        number2 = 4
        expected_result = 6

        # act:
        actual_result = calc.add(number1, number2)

        # assert:
        self.assertEqual(actual_result, expected_result)

    def test_two_positive_floats_return_positive_floats(self):
        # arrange:
        number1 = 2.5
        number2 = 4.75
        expected_result = 7.25

        # act:
        actual_result = calc.add(number1, number2)

        # assert:
        self.assertEqual(actual_result, expected_result)

    # edge cases
    def test_positive_int_and_positive_float_return_positive_float(self):
        # arrange:
        number1 = 2.5
        number2 = 5
        expected_result = 7.5

        # act:
        actual_result = calc.add(number1, number2)

        # assert:
        self.assertEqual(actual_result, expected_result)

    def test_negative_int_and_positive_float_return_float(self):
        # arrange:
        number1 = -2
        number2 = 5.5
        expected_result = 3.5

        # act:
        actual_result = calc.add(number1, number2)

        # assert:
        self.assertEqual(actual_result, expected_result)

    # zeroes
    def test_zero_and_zero_return_zero(self):
        # arrange:
        number1 = 0
        number2 = 0
        expected_result = 0

        # act:
        actual_result = calc.add(number1, number2)

        # assert:
        self.assertEqual(actual_result, expected_result)

        # both negatives
    def test_negative_int_and_negative_float_return_negative_float(self):
        # arrange:
        number1 = -2.5
        number2 = -5
        expected_result = -7.5

        # act:
        actual_result = calc.add(number1, number2)

        # assert:
        self.assertEqual(actual_result, expected_result)

    def test_zero_and_positive_int_returns_positive(self):
        number1 = 0
        number2 = 2
        expected_result = 2
        # act
        actual_result = calc.add(number1, number2)
        self.assertEqual(actual_result, expected_result)

    def test_zero_and_negative_int_returns_negative(self):
        number1 = 0
        number2 = -2
        expected_result = -2
        # act
        actual_result = calc.add(number1, number2)
        self.assertEqual(actual_result, expected_result)

    # ////////////////////////////
    # write tests for subtract
    def test_zero_and_negative_int_returns_positive(self):
        number1 = 0
        number2 = -2
        expected_result = 2
        actual_result = calc.subtract(number1, number2)
        self.assertEqual(actual_result, expected_result)

    def test_negative_int_and_zero_returns_negative(self):
        number1 = -2
        number2 = 0
        expected_result = -2
        actual_result = calc.subtract(number1, number2)
        self.assertEqual(actual_result, expected_result)

    def test_negative_int_and_negative_returns_negative(self):
        number1 = -2
        number2 = -2
        expected_result = 0
        actual_result = calc.subtract(number1, number2)
        self.assertEqual(actual_result, expected_result)

    def test_big_negative_int_and_small_negative_int_return_negative_int(self):
        number1 = -5
        number2 = -2
        expected_result = -3
        # act
        actual_result = calc.subtract(number1, number2)
        self.assertEqual(actual_result, expected_result)

    def test_small_negative_int_and_big_negative_int_return_positive_int(self):
        number1 = -2
        number2 = -4
        expected_result = 2
        # act
        actual_result = calc.subtract(number1, number2)
        self.assertEqual(actual_result, expected_result)

    def test_small_positive_int_and_big_negative_int_return_positive_int(self):
        number1 = 2
        number2 = -4
        expected_result = 6
        # act
        actual_result = calc.subtract(number1, number2)
        self.assertEqual(actual_result, expected_result)

    # ////////////////////////////
    # write tests for multiply
    def test_multiply_2_by_2_gives_4(self):
        # arrange:
        number1 = 2
        number2 = 2
        expected_answer = 4
        # act:
        actual_answer = calc.multiply(number1, number2)
        # assert:
        self.assertEqual(actual_answer, expected_answer)

    def test_multiply_2_by_3_gives_6(self):
        # arrange:
        number1 = 2
        number2 = 3
        expected_answer = 6
        # act:
        actual_answer = calc.multiply(number1, number2)
        # assert:
        self.assertEqual(actual_answer, expected_answer)

    def test_multiply_with_positive_floats_gives_positive_results(self):
        # arrange, act and assert in one line:
        self.assertEqual(calc.multiply(2.0, 3.0), 6.0)
        self.assertEqual(calc.multiply(3.0, 3.0), 9.0)
        self.assertEqual(calc.multiply(2.0, 2.5), 5.0)
        self.assertEqual(calc.multiply(0.0, 3.0), 0)
        self.assertEqual(calc.multiply(4.0, 3.0), 12.0)

    def test_divide_with_positive_ints_gives_positive_results(self):
        # arrange, act and assert in one:
        self.assertEqual(calc.divide(12, 3), 4)
        self.assertEqual(calc.divide(12, 4), 3)
        self.assertEqual(calc.divide(12, 6), 2)

    def test_int_division_by_zero_raises_exception(self):
        self.assertRaises(ZeroDivisionError, calc.divide,12, 0)
