# Activity 4 - Math functions
# Author: Tianxiang Wang
### Part 1 - Develop a Python program that uses functions to generate an N-length Fibonacci series and compute the factorial of N. Do not use any external packages in this version. Include clear inline comments to show your understanding, then upload your code to GitHub and share the link.
from functools import lru_cache
import math

class Test:
    def __init__(self):
        # need a parameter
        text = "Please enter an integer greater than or equal to 0: "
        n = input(text)
        text = "Invalid. " + text
        while n.isdigit() is False or int(n) < 0:
            n = input(text)

        self.n = int(n)


    def fibonacci_series(self):
        n = self.n
        # cache the function results for identical parameters
        @lru_cache(maxsize=None)
        def fib(m):
            # stopping conditions
            if m <= 1:
                # pop
                return m

            # Fibonacci series shows as F(n) = F(n-1) + F(n-2), use recursive function.
            # push fib(m - 1) and fib(m - 2)
            return fib(m - 1) + fib(m - 2)
        # push fib(i)
        return [fib(i) for i in range(n)]





    def factorial(self):
        n = self.n
        # push and pop
        return math.factorial(n)

        

t = Test()
print(f"fibonacci_series: {t.fibonacci_series()}")
print(f"factorial: {t.factorial()}")
