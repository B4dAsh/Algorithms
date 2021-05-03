def recursive_factorial(num) -> int:
    """
        Recursive Factorial.

        A factorial of a given number n is equal to the product of all the 
        natural numbers equal to or smaller than n.
    """
    if num < 0:
        return None
    elif num < 2:
        return 1

    return num * recursive_factorial(num-1)


if __name__ == "__main__":
    # Tests
    assert recursive_factorial(-72) == None
    assert recursive_factorial(0) == 1
    assert recursive_factorial(1) == 1
    assert recursive_factorial(3) == 6
    assert recursive_factorial(5) == 120
    assert recursive_factorial(13) == 6227020800
