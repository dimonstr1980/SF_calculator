import math


class Calculator:
    def adding(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def modulus(self, x, y):
        return x % y

    def square(self, x):
        return x * x

    def square_root(self, x):
        if x >= 0:
            return int(x ** 0.5)

    def factorial(self, x):
        if x == 1:
            return 1
        else:
            return x * math.factorial(x - 1)
