""""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730580155"


def input_word() -> str:
    """Prompts the user to enter a 5-character word"""
    word = input("Enter a 5-character word:")
    if (
        len(word) == 5
    ):  # takes the user's inputted word and runs a different function depending on if it is 5 characters or not
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return word


def input_letter() -> str:
    """Prompts the user to enter a single character"""
    letter = input("Enter a single character:")
    if (
        len(letter) == 1
    ):  # takes the user's inputted character and runs a different function depending on if it is 1 character or not
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()
        return letter


def contains_char(word: str, letter: str) -> None:
    """Searches for a given character in a given word"""
    print(
        "Searching for", letter, "in", word
    )  # tells the user that the function is searching for their letter in their word
    count = 0  # counts up how many instances the letter is found in the word
    if (
        word[0] == letter
    ):  # adds 1 to count depending on if the letter is found at this index
        count += 1
        print(letter, "found at index 0")
    if (
        word[1] == letter
    ):  # adds 1 to count depending on if the letter is found at this index
        count += 1
        print(letter, "found at index 1")
    if (
        word[2] == letter
    ):  # adds 1 to count depending on if the letter is found at this index
        count += 1
        print(letter, "found at index 2")
    if (
        word[3] == letter
    ):  # adds 1 to count depending on if the letter is found at this index
        count += 1
        print(letter, "found at index 3")
    if (
        word[4] == letter
    ):  # adds 1 to count depending on if the letter is found at this index
        count += 1
        print(letter, "found at index 4")
    if count == 1:
        print(count, "instance of", letter, "found in", word)
    elif count == 0:
        print("No instances of", letter, "found in", word)
    else:
        print(count, "instances of", letter, "found in", word)


def main() -> (
    None
):  # bundles up all previously defined functions into one function that's easy to use
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":  # calls main and makes it possible to run it as a module
    main()
