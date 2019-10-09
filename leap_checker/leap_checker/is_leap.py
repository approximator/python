"""
The Leap Year Checker

Author: Approximator
"""


def is_leap(year: int) -> bool:
    """
    Check if provided year is leap
    :param year: year to check
    :return: True if the year is leap, False otherwise
    """
    if year % 4 != 0:
        return False
    return year % 100 != 0 or year % 400 == 0
