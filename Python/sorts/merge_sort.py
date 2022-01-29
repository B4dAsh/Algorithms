def merge_sort(arr) -> list:
    """
        Merge Sort.
        Time complexity - O(nlogn) | Ω(nlogn)
        Space complexity - O(n)

        Merge sort is a divide-and-conquer sorting algorithm where on each 
        call iterable is divided in two and merge sort is applied on both 
        halves which are then merged into one.
    """

    # If there's only one element in the array.
    if len(arr) <= 1:
        return arr

    # Check for tuple.
    if isinstance(arr, tuple):
        return tuple(merge_sort(list(arr)))

    # Call merge sort on each partition.
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    arr = []

    i = j = 0

    while i < len(left) and j < len(right):
        # Append whichever is smaller element.
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    # Check for leftover elements and add them.
    if i < len(left):
         arr.extend(left[i:])
    elif j < len(right):
        arr.extend(right[j:])

    return arr


if __name__ == "__main__":
    # Tests
    assert merge_sort([]) == []
    assert merge_sort([9]) == [9]
    assert merge_sort((82, 45)) == (45, 82)
    assert merge_sort((35.59, 67, 91, 3, 69, 34.2)) == (3, 34.2, 35.59, 67, 69, 91)
    assert merge_sort([3, 5, 6, 4, 7, 8, 1, 9, 10, 7, 3]) == [1, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]
