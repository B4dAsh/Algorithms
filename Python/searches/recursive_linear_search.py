def linear_search_recursive(item, val, index=0) -> int:
    """
        Recursive Linear Search.
        Time complexity - O(n) | Ω(1)
        Space complexity - O(n)

        Recursive linear search, like normal linear search is a simple 
        searching algorithm except recursion is used instead of the 
        loops. It searches the item for specified value by recursing over 
        it, which means every element is checked one by one on each call, 
        If the element is found, the index at which its found is returned. 
        If element does not exist -1 is returned.
    """

    # If item is int or float convert item and value to str for comparison.
    if isinstance(item, int) or isinstance(item, float):
        item = str(item)
        val = str(val)

    # If index has overflowed.
    if index == len(item):
        return -1

    if item[index] == val:
        return index

    return linear_search_recursive(item, val, index + 1)


if __name__ == "__main__":
    # Tests
    assert linear_search_recursive(2546786, 1) == -1
    assert linear_search_recursive(3857234, 8) == 1
    assert linear_search_recursive(455918.35, 3) == 7
    assert linear_search_recursive("linear_search_rocks", "r") == 5

    assert linear_search_recursive([], 1) == -1
    assert linear_search_recursive([3, 7, 8, 9, 0, 1, 2], 4) == -1
    assert linear_search_recursive([2, 5, 7, 5, 8, 34, 64, 23, 73, 93], 7) == 2
    assert linear_search_recursive(["String", '😊', 34, False, 46.2, None], None) == 5
    assert linear_search_recursive(["String", '😊', 34, False, 46.2, None], '😊') == 1
