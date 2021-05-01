def binary_search(arr, val) -> int:
    """
        Binary Search.
        Time complexity - O(logn) | Ω(1)
        Space complexity - O(n)

        Binary search requires a sorted array. On first iteration middle 
        element is selected as the pivotal element.

        On each subsequent iteration:
            * Check If the pivot is equal to the value being searched
            Terminate if it is and return the index of pivot.
            * Else if pivotal element is smaller than value being searched 
            then continue the loop by selecting a new pivot in the array 
            which neglects all elements equal to or smaller than the 
            current pivot.
            * Else if the pivotal element is greater than the value 
            continue loop by selecting a new pivot in the array which 
            neglects all the elements equal to or greater than the current 
            pivot.
            * In case the array is divided until there's only a single 
            element left which is also not equal to the value, it means 
            that the element is not in the array and -1 is returned.

        Binary Search, on each subsequent iteration divides the array in 
        half and hence it is much efficient than Linear
        search where all the elements are checked one by one.
    """

    lower = 0
    upper = len(arr) # Since integer division is being used which is
    # essentially math.floor(), this won't trigger IndexError.

    # As the loop goes on upper and lower values tend to approach each 
    # other to the point where they are same i.e. single element is
    # left in the array and if that isn't the value being searched, loop
    # should end with -1 returned.
    while lower < upper:

        i = (lower + upper) // 2 # Set middle element as pivot.

        if arr[i] == val: # Check if pivot is value being searched.
            return i
        elif arr[i] > val: # Ignore larger elements if pivot is larger than value
            upper = i
        elif arr[i] < val: # Ignore smaller elements if pivot is smaller than value
            lower = i+1

    return -1


if __name__ == "__main__":
    # Tests
    assert binary_search([], 8) == -1
    assert binary_search([3, 64, 7, 23, 75, 92], 8) == -1
    assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == 0
    assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 9
    assert binary_search((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 4) == 4

    assert binary_search(["str1", "str2", "str3", "str4", "str5"], "str3") == 2
    