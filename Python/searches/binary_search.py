def binary_search(arr: list, val: object) -> int:
    """
        Binary Search - O(logn) / Ω(1).

        Binary search requires a sorted array. On first iteration middle element is selected
        as the pivotal element.

        On each subsequent iteration:
            * Check If the pivot is equal to the value being searched, Terminate if it is and return the index of pivot.
            * Else if pivotal element is smaller than value being searched then continue the loop by 
            selecting a new pivot in the array which neglects all elements equal to or smaller than the current pivot.
            * Else if the pivotal element is greater than the value continue loop by selecting a new pivot 
            in the array which neglects all the elements equal to or greater than the current pivot.
            * In case the array is divided until there's only a single element left which is not equal to the value,
            it means that the element is not in the array and -1 is returned.

        Binary Search, on each subsequent iteration divides the array in half and hence it is much efficient than Linear
        search where all the elements are checked one by one.

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
    # Tests
    sortedArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search(sortedArr, 4) == 4
    