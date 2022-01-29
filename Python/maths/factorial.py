def factorial(num) -> int:
    """
        Factorial.

        A Factorial of a given number is defined as the product of all the natural 
        numbers equal to or smaller than it i.e n * (n-1) * (n-2) ... * 2 * 1.
    """

    if num < 0:
        raise ValueError("Factorial is only defined for whole numbers.")
    elif num < 2:
        return 1

    fact = 2

    for i in range(3, num+1):
        fact *= i

    return fact


if __name__ == "__main__":
    # Tests
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(13) == 6227020800
    # assert factorial(-7) == None # This will raise ValueError.
