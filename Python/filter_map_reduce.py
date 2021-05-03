def filter(func, iterable) -> list:
    """
        Filter.

        Filters the iterable based on given function.
    """

    if isinstance(iterable, tuple):
        return tuple(filter(func, list(iterable)))

    return [item for item in iterable if func(item)]


def map(func, iterable):
    """
        Map.

        Applies the function to each element of the array.
    """

    if isinstance(iterable, tuple):
        return tuple(map(func, list(iterable)))

    return [func(item) for item in iterable]


def reduce(func, iterable):
    """
        Reduce.

        Based on given function, returns single value.
    """

    if len(iterable) == 0:
        return None

    final = iterable[0]

    for i in range(1, len(iterable)):
        final = func(final, iterable[i])

    return final


if __name__ == "__main__":
    # Tests
    assert filter(lambda a: a == 1, []) == []
    assert filter(lambda a: a != 1, [1]) == []
    assert filter(lambda a: a <= 1, [1]) == [1]
    assert filter(lambda a: a >= 0, [-2, 5, 0, -3, 9, -4, 6]) == [5, 0, 9, 6]
    assert filter(lambda a: a <= 0, (-2, 5, 0, -3, 9, -4, 6)) == (-2, 0, -3, -4)

    assert map(lambda a: a + 2, []) == []
    assert map(lambda a: a - 3, [8]) == [5]
    assert map(lambda a: a % 2, [10, 9, 8, 7, 6]) == [0, 1, 0, 1, 0]
    assert map(lambda a: a * 2, [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
    assert map(lambda a: a ** 2 , (1, 2, 3, 4, 5)) == (1, 4, 9, 16, 25)

    assert reduce(lambda a, b: a * b, []) == None
    assert reduce(lambda a, b: a * b, [4]) == 4
    assert reduce(lambda a, b: a + b, [1, 3, 5, 6, 7, 9, 19]) == 50
    assert reduce(lambda a, b: a + b, (5, 7, 15, 19, 2, 22, 14)) == 84
