# Activity 3 - Math functions
# Author: Tianxiang Wang
### Part 1 - Develop a Python program that uses functions to generate an N-length Fibonacci series and compute the factorial of N. Do not use any external packages in this version. Include clear inline comments to show your understanding, then upload your code to GitHub and share the link.


def fibonacci_series(n):
    # cache[i] stored F(i)
    cache = [None] * (n + 1)

    def fib(m):
        # stopping conditions
        if m <= 1:
            return m

        # reuse cache
        if cache[m] is not None:
            return cache[m]

        # Fibonacci series shows as F(n) = F(n-1) + F(n-2), use recursive function.
        cache[m] = fib(m - 1) + fib(m - 2)
        return cache[m]

    return [fib(i) for i in range(n)]


# print(fibonacci_series(6))

# F(n) = F(n - 1) * n
def factorial(n):
    # set the stopping condition.
    if n <= 0:
        return "'n' must be larger than 0"
    if n <= 2:
        return n
    return factorial(n - 1) * n

# print(factorial(5))

### Part2 - For the second version, update your program by using built-in packages such as "Math" to enhance or simplify your calculations. Upload this updated version to GitHub as well.

from functools import lru_cache

def fibonacci_series_b(n):

    @lru_cache(maxsize=None)
    def fib(m):
        # stopping conditions
        if m <= 1:
            return m

        # Fibonacci series shows as F(n) = F(n-1) + F(n-2), use recursive function.
        return fib(m - 1) + fib(m - 2)

    return [fib(i) for i in range(n)]


print(fibonacci_series_b(6))

import math

print(math.factorial(5))