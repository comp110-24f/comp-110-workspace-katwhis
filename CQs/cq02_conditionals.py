"""Challenge Question 2"""

__author__ = "730580155"


def guess_a_number() -> None:
    """guesses a number"""
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was", x)
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is", secret)
    elif x > secret:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
