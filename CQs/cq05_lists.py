"""Mutating Functions"""

__author__ = "730580155"


def manual_append(list_value: list[int], number: int) -> None:
    """Appends an int to an existing list"""
    list_value.append(number)


def double(list_value: list[int]) -> None:
    """Doubles all the values in a list"""
    idx = 0
    while idx < len(list_value):
        list_value[idx] = list_value[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
