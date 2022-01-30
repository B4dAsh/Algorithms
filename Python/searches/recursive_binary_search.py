def binary_search_recursive(arr, val, lower=0, upper=None):
    """
        Recursive Binary Search.
        Time complexity - O(logn) | Ω(1)
        Space complexity - O(n)

        Recursive binary search, just like normal binary search requires a 
        sorted array. On first iteration select middle element as the pivot 
        and then-

        On each subsequent iteration:
            * Check If the pivot is equal to the value being searched 
            Terminate if it is and return the index of pivot.
            * Else if pivotal element is smaller than value being searched 
            then run binary search again while neglecting all elements 
            equal or smaller than the pivot.
            * Else if the pivotal element is greater than the value 
            run binary search neglecting all elements equal to greater than 
            the pivot.
            * If there's only a single element left in the iterable which means 
            that the element being searched does not exist within the array, 
            in which case return -1.

        Binary Search, on each subsequent iteration divides the array in half 
        and hence it is much efficient than Linear search where all the elements 
        have to be checked one by one. Although this recursive implementation does 
        not provide any advantage over the iterative approach, It sure is cooler of 
        the two! :p
    """

    # For the first call. This is a workaround 
    # since default value assignment doesn't work if it depends upon 
    # another element being passed into the function...
    if upper is None:
        upper = len(arr)

    p = (lower + upper) // 2 # Set pivot.

    if arr[p] == val: # Check if pivot is value being searched.
        return p;
    elif len(arr[lower: upper+1]) <= 1: # If only one element is left.
        return -1
    elif arr[p] > val: # If pivot is larger, run search neglecting larger elements.
        return binary_search_recursive(arr, val, lower, p-1)
    elif arr[p] < val: # If pivot is smaller, run search neglecting smaller elements.
        return binary_search_recursive(arr, val, p+1, upper)


if __name__ == "__main__":
    # Tests
    assert binary_search_recursive([3, 64, 7, 23, 75, 92], 8) == -1
    assert binary_search_recursive([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0) == 0
    assert binary_search_recursive([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 9
    assert binary_search_recursive((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 4) == 4

    assert binary_search_recursive(["str1", "str2", "str3", "str4", "str5"], "str3") == 2
