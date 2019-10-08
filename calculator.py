"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def division(first_term, second_term):
    try:
        return first_term / second_term
    except ZeroDivisionError:
        return None
