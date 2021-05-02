def bubble_sort(item) -> list:
    """
        Bubble Sort.
        Time complexity - O(n^2) - All values are in reverse | Ω(n) - Already sorted.
        Space complexity - O(n)

        Bubble sort is a basic sorting algorithm. It checks on two elements
        at a time in iterable and swaps them if they are out of order. 
        Therefore, on each subsequent iteration largest element gets sent 
        to the end of the array.
    """

    # If item passed is a tuple.
    if isinstance(item, tuple):
        return tuple(bubble_sort(list(item)))

    swap = True

    while swap: # While elements are out of order

        swap = False
        
        for i in range(0, len(item)-1, 1): # Iterate over the iterable,
            if item[i] > item[i+1]: # Finding out of order elements,
                item[i], item[i+1] = item[i+1], item[i] # & swapping them.
                swap = True
        
    return item


if __name__ == "__main__":
    # Tests
    assert bubble_sort([]) == []
    assert bubble_sort([9]) == [9]
    assert bubble_sort((82, 45)) == (45, 82)
    assert bubble_sort((35.59, 67, 91, 3, 69, 34.2)) == (3, 34.2, 35.59, 67, 69, 91)
    assert bubble_sort([3, 5, 6, 4, 7, 8, 1, 9, 10, 7, 3]) == [1, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]

