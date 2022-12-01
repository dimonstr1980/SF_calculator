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
    
    def task_1(a, d, c):
        ans = (c - d / 5 + math.sqrt(321)) / (1 + a * 3)
        return ans

    def task_2(a, d, c):
        ans = (math.log10(c / 3) - d + 25) / (a * 5 - 1)
        return ans

    def task_3(a, d, c):
        ans = (c / 2 + math.log(d) - 35) / (a * 5 + 1)
        return ans

    def task_4(a, d, c):
        ans = (math.tan(c) + d / 32) / (a / 3 + 1)
        return ans

    def task_5(a, d, c):
        ans = (c / 5 - d + 1) / (c + math.tan(2 * a))
        return ans

    def task_6(a, d, c):
        ans = (math.sqrt(25 * c) + d - 3) / (d - a * a + 1)
        return ans

    def task_7(a, d, c):
        ans = (5 * math.log10(c) + 3 * d - 32) / (a * a + 1)
        return ans

    def task_8(a, d, c):
        ans = (c * d - math.log(4 * 3 * a)) / (c + a - 1)
        return ans
