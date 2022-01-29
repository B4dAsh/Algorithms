def fibonacci(limit) -> list:
    """
        Fibonacci Sequence.

        A Fibonacci sequence is a sequence where each term is genrated by 
        adding previous two terms, first two terms are generally 0 
        and 1. This algorithm genrates all the terms not exceeding given 
        limit and returns it as a list.
    """

    # Limit can't be negative.
    if limit < 0:
        return []

    first = 0
    second = 1
    fib = [first]

    while second <= limit:
        fib.append(second)
        second = first + second
        first = second - first

    return fib


if __name__ == "__main__":
    # Tests
    assert fibonacci(-45) == []
    assert fibonacci(0) == [0]
    assert fibonacci(1) == [0, 1, 1]
    assert fibonacci(144) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    assert fibonacci(200000) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 
        144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 
        28657, 46368, 75025, 121393, 196418]
