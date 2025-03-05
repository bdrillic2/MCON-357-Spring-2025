import unittest
import sys
from calculate_factorial import factorial_recursive

class test_factorial(unittest.TestCase):

    def test_0_factorial(self):
        self.assertEqual(factorial_recursive(0), 1)

    def test_1_factorial(self):
        self.assertEqual(factorial_recursive(1), 1)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            factorial_recursive(-5)
        self.assertEqual(str(context.exception), "Negative numbers are not allowed")

    def test_fraction_factorial(self):
        with self.assertRaises(ValueError) as context:
            factorial_recursive(4.27)
        self.assertEqual(str(context.exception), "Number must be an integer")

    def test_positive_factorial(self):
        self.assertEqual(factorial_recursive(4), 24)

    def test_large_factorial(self):
        self.assertEqual(factorial_recursive(18), 6402373705728000)

    def test_below_recursion_limit(self):
        safe_input = 100

        try:
            factorial_recursive(safe_input)  # Shouldn't raise an error
        except RecursionError:
            self.fail("Number exceeded recursion limit")

    def test_above_recursion_limit(self):
        limit = sys.getrecursionlimit()
        risky_input = limit + 10  # Beyond the safe limit

        with self.assertRaises(RecursionError):
            factorial_recursive(risky_input)  # Should raise an error

if __name__ == '__main__':
    unittest.main()
