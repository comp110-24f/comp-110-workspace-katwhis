"""CQ03: Practing using a while loop to iterate over a string"""

__author__ = "730580155"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0
    index = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
