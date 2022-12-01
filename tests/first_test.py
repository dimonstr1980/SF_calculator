import pytest
import math
import task
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
        
    def test_1(self):
        a, d, c = 3, 5, 7
        ans = (c - d / 5 + math.sqrt(321)) / (1 + a * 3)
        self.assertEqual(task.task_1(3, 5, 7), ans)

    def test_2(self):
        a,d,c = 2,4,6
        ans = (math.log10(c/3)-d+25)/(a*5-1)
        self.assertEqual(task.task_2(2, 4, 6), ans)

    def test_3(self):
        a,d,c = 9,8,7
        ans = (c/2+math.log(d)-35)/(a*5+1)
        self.assertEqual(task.task_3(9, 8, 7), ans)

    def test_4(self):
        a,d,c = 3,4,5
        ans = (math.tan(c)+d/32)/(a/3+1)
        self.assertEqual(task.task_4(3, 4, 5), ans)

    def test_5(self):
        a,d,c = 2,3,4
        ans = (c/5-d+1)/(c+math.tan(2*a))
        self.assertEqual(task.task_5(2, 3, 4), ans)

    def test_6(self):
        a,d,c = 5,6,3
        ans = (math.sqrt(25*c)+d-3)/(d-a*a+1)
        self.assertEqual(task.task_6(5, 6, 3), ans)

    def test_7(self):
        a,d,c = 6,7,8
        ans = (5*math.log10(c)+3*d-32)/(a*a+1)
        self.assertEqual(task.task_7(6, 7, 8), ans)

    def test_8(self):
        a,d,c = 2,9,5
        ans = (c*d-math.log(4*3*a))/(c+a-1)
        self.assertEqual(task.task_8(2, 9, 5), ans)
        
