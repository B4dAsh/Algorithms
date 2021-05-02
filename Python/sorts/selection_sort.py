def selection_sort(item) -> list:
    """
        Selection Sort.
        Time complexity - O(n^2) | Ω(n^2)
        Space complexity - O(n)

        Selection sort divides iterable in two - sorted and unsorted parts, 
        On each iteration it selects the largest (or the smallest) element 
        and then swaps it with the last unsorted element in the iterable.
    """

    # If item passed is a tuple.
    if isinstance(item, tuple):
        return tuple(selection_sort(list(item)))

    for i in range(len(item)): # Iterate over the iterable.

        # Point to last element of unsorted iterable.
        max_index = len(item) - i - 1

        # Iterate on unsorted part of the iterable.
        for j in range(len(item)-i):
            if item[j] > item[max_index]:
                max_index = j # Set pointer to the larger element.

        item[len(item)-i-1], item[max_index] = item[max_index], item[len(item)-i-1] # Swap.

    return item


if __name__ == "__main__":
    # Tests
    assert selection_sort([]) == []
    assert selection_sort([9]) == [9]
    assert selection_sort((82, 45)) == (45, 82)
    assert selection_sort((35.59, 67, 91, 3, 69, 34.2)) == (3, 34.2, 35.59, 67, 69, 91)
    assert selection_sort([3, 5, 6, 4, 7, 8, 1, 9, 10, 7, 3]) == [1, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]

