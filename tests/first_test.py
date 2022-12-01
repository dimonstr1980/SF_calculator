import pytest
import math
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
    # Пример 1
    def task_1(a, d, c):
        ans = (c - d / 5 + math.sqrt(321)) / (1 + a * 3)
        return ans

    # Пример 2
    def task_2(a, d, c):
        ans = (math.log10(c / 3) - d + 25) / (a * 5 - 1)
        return ans

    # Пример 3
    def task_3(a, d, c):
        ans = (c / 2 + math.log(d) - 35) / (a * 5 + 1)
        return ans

    # Пример 4
    def task_4(a, d, c):
        ans = (math.tan(c) + d / 32) / (a / 3 + 1)
        return ans

    # Пример 5
    def task_5(a, d, c):
        ans = (c / 5 - d + 1) / (c + math.tan(2 * a))
        return ans

    # Пример 6
    def task_6(a, d, c):
        ans = (math.sqrt(25 * c) + d - 3) / (d - a * a + 1)
        return ans

    # Пример 7
    def task_7(a, d, c):
        ans = (5 * math.log10(c) + 3 * d - 32) / (a * a + 1)
        return ans

    # Пример 8
    def task_8(a, d, c):
        ans = (c * d - math.log(4 * 3 * a)) / (c + a - 1)
        return ans
