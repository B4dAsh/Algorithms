def combination(n, r):
    """
        Combinations.
        Time complexity - O(n) | Ω(1)

        A combination of a number n is defined as selection of r elemental subsets 
        from a set with the cardinality of n, n ≥ r ≥ 0 and where the order of 
        selection does not matter. It is calculated with the formula n! / ((n-r)! * r!).
    """

    from functools import reduce

    if n < r or r < 0:
        raise ValueError("Combinations are not defined for provided values.")

    comb = 1

    for i in range(n, max(n-r, r), -1):
        comb *= i

    return comb // reduce(lambda a, b: a*b, [i for i in range(min(n-r, r), 0, -1)], 1)


if __name__ == "__main__":
    # Tests
    assert combination(0, 0) == 1
    assert combination(3, 2) == 3
    assert combination(5, 2) == 10
    assert combination(7, 3) == 35
    assert combination(10, 4) == 210

    # Following will raise ValueErrors
    # combination(-4, 2)
    # combination(5, -3)
    # combination(8, 10)

    # # Prints rows of Pascal's triangle till given limit.
    # for i in range(1, 10):
    #     print(combination(10, i), end=" | ")
    # print()
    # [ print(combination(10, i) + " | ") for i in range(1, 10) ]
