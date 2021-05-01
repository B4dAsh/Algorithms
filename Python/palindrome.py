def is_palindrome(object) -> bool:
    """
        Palindrome Checker.
        Time complexity - O(n/2) -> O(n) | Ω(n/2) -> Ω(n)
        Space complexity - O(n)

        This function checks whether the object is palindrome or not and 
        and based on that returns a boolean value.

        * Case insensitive in case of Strings.
        * Works on integers, floats, lists and tuples.
    """

    # If object is a string, make it lowercase to achieve
    # case insensitivity.
    if isinstance(object, str):
        object = object.lower()
    # Convert the object to a string if it is an integer.
    elif isinstance(object, int):
        object = str(object)
    # Convert object to a string if its a float and remove the decimal point.
    elif isinstance(object, float):
        object = str(object).replace(".", "")

    # Compare element at each index to the element situated at that index's
    # complement index. If all of elements are equal return true else
    # return false
    return all(object[i] == object[~i] for i in range(len(object)//2))


if __name__ == "__main__":

    # Tests
    assert is_palindrome("") == True
    assert is_palindrome(7) == True

    assert is_palindrome("lol") == True
    assert is_palindrome("Abba") == True
    assert is_palindrome("palindrome") == False

    assert is_palindrome(343) == True
    assert is_palindrome(34.43) == True
    assert is_palindrome(34) == False

    assert is_palindrome([3, 5, 6, 5, 3]) == True
    assert is_palindrome(('3', '5', '6', '5', '3')) == True
    assert is_palindrome([True, False, True, False, True]) == True
    assert is_palindrome([43, False, "String", "String", False, 43]) == True
    assert is_palindrome([43, False, "String", False, "String", 43]) == False