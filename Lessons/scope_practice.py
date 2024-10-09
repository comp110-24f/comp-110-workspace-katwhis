def remove_chars(msg: str, char: str) -> str:
    """Returns a copy of msg with all instances of char removed"""
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    # if running this file itself and not on another file, you want this code to be run
    word = "yoyo"
    print(remove_chars(word, "o"))
    print(word)
