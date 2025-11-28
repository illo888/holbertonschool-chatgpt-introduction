#!/usr/bin/python3
"""
This module calculates the factorial of a given number using recursion.
"""
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Description:
        This function computes the factorial of a number n, which is the
        product of all positive integers less than or equal to n.
        It uses recursive calls until reaching the base case (n == 0).

    Parameters:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of n. Returns 1 if n is 0 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
