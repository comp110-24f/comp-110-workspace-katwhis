"""Summing the elements of a list using different loops"""

__author__ = "730580155"


def w_sum(vals: list[float]) -> float:
    """uses a while loop to get sum"""
    idx = 0
    sum_val = 0.0
    while idx < len(vals):
        sum_val += vals[idx]
        idx += 1
    return sum_val


def f_sum(vals: list[float]) -> float:
    """uses a for loop to get sum"""
    sum_val = 0.0
    for num in vals:
        sum_val += num
    return sum_val


def f_range_sum(
    vals: list[float],
) -> float:
    """uses the range of a list in a for loop to get sum"""
    sum_val = 0.0
    for i in range(0, len(vals)):
        sum_val += vals[i]
    return sum_val
