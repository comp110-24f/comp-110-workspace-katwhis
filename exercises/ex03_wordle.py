"""EX03: Wordle"""

__author__ = "730580155"


def input_guess(
    secret_word_len: int,
) -> (
    str
):  # user enters word and then the function makes sure it has the correct amount of characters
    """Prompts a user to enter a word with an certain number of characters"""
    word = input(f"Enter a {secret_word_len} character word:")
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again:")
        # said something about missing something but then went away
        # doesn't work in repl but works in trailhead
        # now it works fine and I didn't do anything
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks whether a character is present at any index of a word"""
    assert len(char_guess) == 1
    idx = 0
    while idx < len(secret_word):
        if (
            char_guess == secret_word[idx]
        ):  # if the character is in the word, it will return true
            return True
        idx += 1
    return False  # if guess isn't in word it will return false


def emojified(user_guess: str, secret_word: str) -> str:
    """Compares 2 strings to see if the characters in the guess match the secret word"""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_str = ""
    idx = 0
    while idx < len(user_guess):  # adds green box if character is in the correct place
        if user_guess[idx] == secret_word[idx]:
            emoji_str += GREEN_BOX
        elif (
            contains_char(secret_word, user_guess[idx]) == True
        ):  # adds yellow box if character is in the word but in the wrong place
            emoji_str += YELLOW_BOX
        else:  # adds white box if character is not in word
            emoji_str += WHITE_BOX
        idx += 1
    return emoji_str


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    idx = 0
    while idx < 6:  # goes through 6 guesses for word
        print(f"=== Turn {idx + 1}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        idx += 1
        if guess == secret:  # prints if user guesses secret word
            print(f"You won in {idx}/6 turns!")
            idx = 7
        else:
            if idx == 6:  # prints if user doesn't guess secret word
                print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
