def linear_search(arr, val) -> int:
    """
        Linear Search - O(n) / Ω(1).

        Linear search searches an array for specified value sequentially meaning each node is checked once.
        It returns index of position where it finds the value or -1 if the value does not exists in the array.
    """

    for i in range(len(arr)):
        if val == arr[i]:
            return i

    return -1


if __name__ == "__main__":
    # Tests
    arr = [2, 5, 7, 5, 8, 34, 64, 23, 73, 93]
    assert linear_search(arr, 7) == 2
    assert linear_search(arr, 93) == 9


