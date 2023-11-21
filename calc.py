"""
Simple Calculator Module

This module defines a basic calculator class and its corresponding unit tests.
"""

import unittest


class Calculator:
    """A simple calculator class."""

    def add(self, x, y):
        """Addition operation."""
        return x + y

    def subtract(self, x, y):
        """Subtraction operation."""
        return x - y

    def multiply(self, x, y):
        """Multiplication operation."""
        return x * y

    def divide(self, x, y):
        """Division operation."""
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

    def power(self, base, exponent):
        """Exponential operation."""
        return base ** exponent


class CalculatorTest(unittest.TestCase):
    """Test case for the Calculator class."""

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """Test addition."""
        self.assertEqual(10, self.calc.add(3, 7), "The addition is wrong")

    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(12, self.calc.subtract(15, 3), "Subtraction is wrong")

    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(30, self.calc.multiply(5, 6), "Multiplication is wrong")

    def test_divide(self):
        """Test division."""
        self.assertEqual(3, self.calc.divide(6, 2), "Division is wrong")

    def test_power(self):
        """Test exponentiation."""
        self.assertEqual(64, self.calc.power(2, 6), "Power calculation is wrong")


if __name__ == '__main__':
    unittest.main()
