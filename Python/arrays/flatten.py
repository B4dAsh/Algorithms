def flatten(arr) -> list:
    """
        Flatten.

        Transforms multidimensional arrays to one dimensional array i.e. 
        flattens them.
    """

    flat = []

    for element in arr:
        if isinstance(element, list): # If element is a list,
            flat.extend(flatten(element)) # Flatten it.
        else:
            flat.append(element) # Add to the list

    return flat


if __name__ == "__main__":
    # Tests
    assert flatten([]) == []
    assert flatten([1]) == [1]
    assert flatten([1, [3, 4], 5]) == [1, 3, 4, 5]
    assert flatten([1, [3, [5, 6, 7]], 5]) == [1, 3, 5, 6, 7, 5]
    assert flatten([1, [3, [5], [6, 7]], 5]) == [1, 3, 5, 6, 7, 5]
    assert flatten([1, [3], [[5, 6], [5, 6, 7], [[[4]]]], 5]) == [1, 3, 5, 6, 5, 6, 7, 4, 5]
