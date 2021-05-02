def is_prime(number) -> bool:
    """
        Prime Number Checker.
        Time Complexity - O(n^1/2)
        Space Complexity - O(1)
    """

    # If number is less than one or the number is even.
    if (number <= 1) or (number % 2 == 0 and number > 2): 
        return False

    i = 3

    while i * i <= number:
        if number % i == 0: # If number is perfectly divisible.
            return False
        i += 2 # Increment by 2 to skip over even numbers

    return True


if __name__ == "__main__":
    # Tests
    assert is_prime(-7) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(9) == False

    assert is_prime(17) == True
    assert is_prime(81) == False
    assert is_prime(255) == False
    assert is_prime(468911111) == True
