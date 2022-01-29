def assert_(expr1, expr2, errorMsg="") -> bool:
    """
        Assertion.
        Time complexity - O(1) | Ω(1)

        Simple assertion script that raises assertion error if both values 
        are not equal. Would work on custom objects too provided that 
        obj.__eq__() method is defined.
    """

    if expr1 != expr2:
        raise AssertionError(errorMsg)

    return True


if __name__ == "__main__":
    # Tests
    assert_(3, 3)
    assert_("3", "3")
    assert_(True, True)
    assert_(False, False)
    assert_(3>2, 8+9==17)
