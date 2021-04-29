def Assert(expr1: object, expr2: object, errorMsg: str = ""):
    """
        Assert - O(1) / Ω(1)

        Simple assertion script that raises assertion error if both values are not equal.
        Would work on user defined objects too provided that obj.__eq__() method is defined.
        
    """

    if expr1 != expr2:
        raise AssertionError(errorMsg)

    return True


if __name__ == "__main__":
    # Tests
    Assert(3, 3)
    Assert("3", "3")
    Assert(3, "3")