def linear_search(item, val) -> int:
    """
        Linear Search.
        Time complexity - O(n) | Ω(1)
        Space complexity - O(n)

        Linear search is the simplest and most basic searching algorithm. 
        It searches the iterable for specified value by iterating over it,
        which means every element is checked one by one. If the element
        is found, the index at which its found is returned. If element does
        not exists -1 is returned.
    """

    if isinstance(item, int) or isinstance(item, float):
        item = str(item)
        val = str(val)

    for i in range(len(item)):
        if item[i] == val:
            return i

    return -1


if __name__ == "__main__":
    # Tests
    assert linear_search(2546786, 1) == -1
    assert linear_search(3857234, 8) == 1
    assert linear_search(455918.35, 3) == 7
    assert linear_search("linear_search_rocks", "r") == 5
    
    assert linear_search([], 1) == -1
    assert linear_search([3, 7, 8, 9, 0, 1, 2], 4) == -1
    assert linear_search([2, 5, 7, 5, 8, 34, 64, 23, 73, 93], 7) == 2
    assert linear_search(["String", '😊', 34, False, 46.2, None], None) == 5
    assert linear_search(["String", '😊', 34, False, 46.2, None], '😊') == 1