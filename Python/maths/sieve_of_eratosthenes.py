def sieve_of_eratosthenes(limit) -> list:
    """
        Sieve of Eratosthenes.
        Time Complexity - O(nlog(logn))
        Space Complexity - O(n)

        The sieve of eratosthenes is one of the most efficient algorithms 
        to find all the prime numbers not exceeding certain limit.

        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    
    # Return empty list if limit is lower than the smallest prime number.
    if limit < 2:
        return []

    # Set all of the numbers to be prime.
    result = [True for _ in range(0, limit+1)]

    result[0] = result[1] = False

    i = 2 # Start loop from first prime number, which will mark all even
    # numbers to be false.

    while i * i <= limit:
        if result[i]: # If prime,

            # Mark all of its multiple to be false.
            for j in range(i*i, limit + 1, i):
                result[j] = False

        i += 1

    # Return list of indices of all elements who are prime.
    return [n for n in range(len(result)) if result[n]]


if __name__ == "__main__":
    # Tests
    assert sieve_of_eratosthenes(0) == []
    assert sieve_of_eratosthenes(1) == []
    assert sieve_of_eratosthenes(2) == [2]
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    assert sieve_of_eratosthenes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]