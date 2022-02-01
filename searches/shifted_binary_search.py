def shifted_binary_search(arr, val, lower=0, upper=None) -> int:
    """
        Binary Search on shift sorted array.
        Time complexity - O(logn) | Ω(1)
        Space complexity - O(n)

        Special case binary search algorithm for shift sorted arrays.
    """

    if len(arr) == 0: # Check for empty array
        return -1

    if upper is None: # Workaround for first iteration.
        upper = len(arr)

    mid = (lower + upper) // 2

    if arr[mid] == val: # If mid is the value being searched.
        return mid

    # If [lower -> mid] is sorted.
    if arr[lower] < arr[mid]:

        # Check if value is in the array.
        if arr[lower] <= val and arr[mid] >= val:
            return shifted_binary_search(arr, val, lower, mid-1)
        # Else run binary search on larger subarray.
        return shifted_binary_search(arr, val, mid+1, upper)

    # If [mid -> upper] is sorted.
    elif arr[mid] < arr[upper-1]:

        # Check if value is in this array.
        if arr[mid] <= val and arr[upper-1] >= val:
            return shifted_binary_search(arr, val, mid+1, upper)
        # Run binary search on smaller subarray.
        return shifted_binary_search(arr, val, lower, mid-1)

    return -1


if __name__ == "__main__":
    # Tests
    assert shifted_binary_search([], 8) == -1
    assert shifted_binary_search([12, 15, 23, 35, 49, 3, 5, 7, 9], 8) == -1
    assert shifted_binary_search([7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == 3
    assert shifted_binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 9
    assert shifted_binary_search((5, 6, 7, 8, 9, 0, 1, 2, 3, 4), 4) == 9
    assert shifted_binary_search((5, 6, 7, 8, 9, 10, 11, 12, 33, 4), 4) == 9

    assert shifted_binary_search(["str1", "str2", "str3", "str4", "str0"], "str0") == 4
