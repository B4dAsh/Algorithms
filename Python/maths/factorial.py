def factorial(num) -> int:
    """
        Factorial.

        A factorial of a given number n is equal to the product of all the 
        natural numbers equal to or smaller than n.
    """

    if num < 0:
        return None
    elif num < 2:
        return 1

    fact = 2

    for i in range(3, num+1):
        fact *= i

    return fact


if __name__ == "__main__":
    # Tests
    assert factorial(-72) == None
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(13) == 6227020800
