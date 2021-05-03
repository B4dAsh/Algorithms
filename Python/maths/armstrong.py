def is_armstrong(num) -> bool:
    """
        Armstrong Number Checker.

        An armstrong number is a number whose sum of cubes of all the
        digits is equal to the the number itself.
    """

    if num < 0:
        return False

    if num == sum([pow(int(i), 3) for i in str(num)]):
        return True

    return False


if __name__ == "__main__":
    # Tests
    assert is_armstrong(-153) == False
    assert is_armstrong(-7) == False
    assert is_armstrong(0) == True
    assert is_armstrong(1) == True
    assert is_armstrong(9) == False
    assert is_armstrong(68) == False
    assert is_armstrong(153) == True