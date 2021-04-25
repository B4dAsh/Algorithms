def binary_search(arr, val) -> int:
    """
        Binary Search - O(logn) / Ω(1).

        Binary search requires a sorted array, it divides the array by half and gets a pivot element.
        If the pivot is the value, its index is returned, if pivot is smaller than value then the binary
        search is run of new array where elements smaller than pivot are neglected. if pivot is greater
        the elements greater than pivot are neglected. Therefore, on each subsequent iteration array gets
        divided in half and hence it is much quicker than Linear search where we check all the elements.
        Otherwise in case the value is not in the array -1 is returned.
    """

    lower = 0
    upper = len(arr)

    while lower < upper:

        i = (lower + upper) // 2

        if val == arr[i]:
            return i
        elif val < arr[i]:
            upper = i
        elif val > arr[i]:
            lower = i

    return -1


if __name__ == "__main__":
    # Write tests here
    sortedArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search(sortedArr, 4) == 4
    