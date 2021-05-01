def reverse(item) -> object:
    """
        Reversion.
        Time complexity - 
        O(n/2) + O(n) = O(3n/2) -> O(n) For strings, integers and floats. |Ω(n/2) -> Ω(n) - For lists and tuples.

        This algorithms simply reverses the input given to it.
        Along with strings, lists and tuples it works with integers
        and floats too, by using some fancy recursion.
    """

    # If item is a string, convert it to a list since strings are immutable in Python.
    # then, pass it through this function and join the result and return it.
    if isinstance(item, str):
        return "".join(reverse(list(item)))
    # If item is a int, covert it to a string and pass it again through this function,
    # Return the returned result in integer format.
    elif isinstance(item, int):
        return int(reverse(str(item)))
    # If item is a float, do same thing as done with it and just return the result in float than int.
    elif isinstance(item, float):
        return float(reverse(str(item)))

    # Swap the element at index i with complement of i until halfway into the array.
    for i in range(len(item)//2):
        item[i], item[~i] = item[~i], item[i]
        
    return item


if __name__ == "__main__":
    # Tests.
    assert reverse("That's what she said") == "dias ehs tahw s'tahT"
    assert reverse(123456789) == 987654321
    assert reverse(219.73) == 37.912

    assert reverse([33, 64, 73, 89, 93, 71, 29]) == [29, 71, 93, 89, 73, 64, 33]
    assert reverse(['92', '34', '37', '42', '47', '43', '94']) == ['94', '43', '47', '42', '37', '34', '92']
    assert reverse([True, False, True, True, False]) == [False, True, True, False, True]
    assert reverse([57, 'object', True, None, 39.5]) == [39.5, None, True, 'object', 57]