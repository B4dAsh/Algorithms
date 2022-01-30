def permutations(n, r):
    """
        Permutations.
        Time complexity - O(n-r) -> O(n) | Ω(1)

        A permutation is defined as the number of ways in which n objects 
        can be arranged into unique ordered sequences of r objects, n ≥ r ≥ 0. They 
        are calculated with the formula n!/(n-r)! where all of the n objects 
        are unique i.e. there are no repetitions of objects.
    """

    if n < r or r < 0:
        raise ValueError("Permutations are not defined for provided values.")

    perm = 1

    for i in range(n, n-r, -1):
        perm *= i

    return perm


if __name__ == "__main__":
    # Tests
    assert permutations(0, 0) == 1
    assert permutations(3, 3) == 6
    assert permutations(5, 2) == 20
    assert permutations(9, 4) == 3024
    assert permutations(10, 6) == 151200

    # Following will raise ValueErrors.
    # permutations(7, -2)
    # permutations(2, 5)
