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




# F(n) = F(n - 1) * n
def factorial(n):
    # set the stopping condition.
    if n <= 0:
        return "'n' must be larger than 0"
    if n <= 2:
        return n
    return factorial(n - 1) * n



### Part2 - For the second version, update your program by using built-in packages such as "Math" to enhance or simplify your calculations. Upload this updated version to GitHub as well.

from functools import lru_cache

def fibonacci_series_b(n):
    # cache the function results for identical parameters
    @lru_cache(maxsize=None)
    def fib(m):
        # stopping conditions
        if m <= 1:
            return m

        # Fibonacci series shows as F(n) = F(n-1) + F(n-2), use recursive function.
        return fib(m - 1) + fib(m - 2)

    return [fib(i) for i in range(n)]




import math

def factorial_b(n):
    return math.factorial(n)


if __name__ == "__main__":
    x = int(input("Enter a number: "))

    print("Part1:")
    print(f"fibonacci_series({x}) = {fibonacci_series(x)}")
    print(f"factorial({x}) = {factorial(x)}")

    print("Part2:")
    print(f"fibonacci_series_b({x}) = {fibonacci_series_b(x)}")
    print(f"factorial_b({x}) = {factorial_b(x)}")