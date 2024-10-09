"""CQ04 Concatenation File"""

__author__ = "730580155"


def concat(str_1: str, str_2: str) -> str:
    """Returns the concstenation of two input strings"""
    return str_1 + str_2


if __name__ == "__main__":
    word1 = "happy"
    word2 = "tuesday"
    print(concat(word1, word2))
