def insertion_sort(item) -> list:
    """
        Insertion Sort.
        Time complexity - O(n^2) - All values are in reverse | Ω(n) - Already sorted.
        Space complexity - O(n)

        Insertion sort works like sorting a deck of cards. On each 
        iteration you take one element out, shift all elements that are 
        larger and insert the element where it is just larger than the 
        previous element.
    """

    # If item passed is a tuple.
    if isinstance(item, tuple):
        return tuple(insertion_sort(list(item)))

    for i in range(1, len(item)): # Iterate over the iterable.

        current = item[i] # Save current element.

        j = i-1 # Pointer to the previous index

        # While element is smaller than previous element
        while current < item[j] and j >= 0:
            item[j+1] = item[j] # Shift
            j -= 1
        
        item[j+1] = current # Insert element to accurate position.

    return item


if __name__ == "__main__":
    # Tests
    assert insertion_sort([]) == []
    assert insertion_sort([9]) == [9]
    assert insertion_sort((82, 45)) == (45, 82)
    assert insertion_sort((35.59, 67, 91, 3, 69, 34.2)) == (3, 34.2, 35.59, 67, 69, 91)
    assert insertion_sort([3, 5, 6, 4, 7, 8, 1, 9, 10, 7, 3]) == [1, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]

