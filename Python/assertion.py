def Assert(expr1, expr2, errorMsg="") -> bool:
    """
        Assertion.
        Time complexity - O(1) | Ω(1)

        Simple assertion script that raises assertion error if both values
        are not equal. Would work on user defined objects too provided 
        that obj.__eq__() method is defined.
    """

    if expr1 != expr2:
        raise AssertionError(errorMsg)

    return True


if __name__ == "__main__":
    # Tests
    Assert(3, 3)
    Assert("3", "3")
    Assert(True, True)
    Assert(False, False)
    Assert(3>2, 8+9==17)