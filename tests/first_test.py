import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 1

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_division_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 0

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self, 2, 2) == 1

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 2, 2) == 1

    def test_modulus_calculate_correctly(self):
        assert self.calc.modulus(self, 2, 2) == 0

    def test_modulus_calculate_failed(self):
        assert self.calc.modulus(self, 2, 2) == 1

    def test_square_calculate_correctly(self):
        assert self.calc.square(self, 2) == 4

    def test_square_calculate_failed(self):
        assert self.calc.square(self, 2) == 1

    def test_square_root_calculate_correctly(self):
        assert self.calc.square_root(self, 9) == 3

    def test_square_root_calculate_failed(self):
        assert self.calc.square_root(self, 9) == 1

    def test_factorial_calculate_correctly(self):
        assert self.calc.factorial(self, 5) == 120

    def test_factorial_calculate_failed(self):
        assert self.calc.factorial(self, 5) == 1
