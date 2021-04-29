def reverse_string(str: str) -> str:
    """
        Reverses the string just as it is,
        without any formatting.
    """

    str = list(str)

    for i in range(len(str)//2):
        str[i], str[~i] = str[~i], str[i]

    return "".join(str)


if __name__ == "__main__":
    assert reverse_string("That's what she said") == "dias ehs tahw s'tahT"