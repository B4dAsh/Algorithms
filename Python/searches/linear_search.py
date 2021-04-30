def linear_search(arr: list, val: object) -> int:
    """
        Linear Search - O(n) | Ω(1).

        Linear search is the simplest and most basic searching algorithm. 
        It searches the array for specified value by iterating over it,
        which means every element is checked one by one. If the element
        is found, the index at which its found is returned. If element does
        not exists in the array -1 is returned.
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