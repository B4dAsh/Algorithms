def quick_sort(item) -> list:
    """
        Quick Sort.
        Time complexity - O(n^2) | Ω(n)
        Space complexity - O(n)

        Quick sort is a divide-and-conquer sorting algorithm. On each 
        iteration a pivot is selected and then three lists created for 
        elements smaller, equal to and greater than the pivot. Quick 
        sort is then applied on both the smaller and greater lists, 
        Leaving equal list as it is already sorted.
    """

    # If item passed is a tuple.
    if isinstance(item, tuple):
        return tuple(quick_sort(list(item)))

    # Base case.
    if len(item) <= 1:
        return item

    small = []
    eq = []
    large = []

    # Select middle element as pivot.
    pivot = item[len(item) // 2]

    for element in item:
        if element < pivot:
            small.append(element)
        elif element > pivot:
            large.append(element)
        else:
            eq.append(element)

    # Now run quick sort on both thesmaller and larger lists and 
    # join them together and return.
    return quick_sort(small) + eq + quick_sort(large)


if __name__ == "__main__":
    # Tests
    assert quick_sort([]) == []
    assert quick_sort([9]) == [9]
    assert quick_sort((82, 45)) == (45, 82)
    assert quick_sort((35.59, 67, 91, 3, 69, 34.2)) == (3, 34.2, 35.59, 67, 69, 91)
    assert quick_sort([3, 5, 6, 4, 7, 8, 1, 9, 10, 7, 3]) == [1, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]
