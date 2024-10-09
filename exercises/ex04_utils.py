"""EX04 Utility Functions"""

__author__ = "730580155"


def all(int_list: list[int], number: int) -> bool:
    """loops through all numbers in a list and sees if they are all the same as the inputted number"""
    idx = 0
    if int_list == []:  # if list is empty this will return False
        return False
    while idx < len(int_list):
        print(int_list[idx])
        if (
            int_list[idx] != number
        ):  # if one number is not the same as the inputted number, this will return False
            return False
        idx += 1
    return True
    # might need to redo bc it doesn't go through all the numbers
    # i think its fine but the autograder might not like it


def max(int_list: list[int]) -> int:
    """Loops through a list and finds the highest number"""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = int_list[0]  # max starts out as the first number in the ist
    for num in int_list:
        if (
            max_num < num
        ):  # if max is smalller than the number the for loop is currently on, it replaces the max with the current number
            max_num = num
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Sees if two lists are completely equal"""
    if len(list1) != len(
        list2
    ):  # if the lengths are different the lists can't be equal, so this returns False
        return False
    for i in range(0, len(list1)):
        if (
            list1[i] != list2[i]
        ):  # if one of the variables are not the same this returns False
            return False
    return True  # if the for loop completes the lists are completely the same, so this returns True


def extend(list1: list[int], list2: list[int]) -> None:
    """Combines list1 and list 2 into one long list"""
    for num in list2:
        list1.append(num)  # loops through list2 and appends all values into list1
