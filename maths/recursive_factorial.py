def recursive_factorial(num) -> int:
    """
        Recursive Factorial.

        A Factorial of a given number is defined as the product of all the natural 
        numbers equal to or smaller than it i.e n * (n-1) * (n-2) ... * 2 * 1.
    """

    if num < 0:
        raise ValueError("Factorial is only defined for whole numbers.")
    elif num < 2:
        return 1

    return num * recursive_factorial(num-1)


if __name__ == "__main__":
    # Tests
    assert recursive_factorial(0) == 1
    assert recursive_factorial(1) == 1
    assert recursive_factorial(3) == 6
    assert recursive_factorial(5) == 120
    # assert recursive_factorial(-7) == None # This will raise a ValueError.
    assert recursive_factorial(13) == 6227020800
