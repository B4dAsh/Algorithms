import re

def camel_case(str) -> str:
    """
        Camel Case.

        This program coverts string to camel case.
    """

    # Check for empty string.
    if str == "":
        return str

    # Covert to lower case and split string using regex.
    words = re.split("[_%*.\-\s]", str.lower())

    # Join the string after converting each word to title case.
    camelcase = "".join([word.title() for word in words])

    # Return concatenation of first letter to lower case and rest of the string.
    return camelcase[0].lower() + camelcase[1:]


if __name__ == "__main__":
    # Tests
    assert camel_case("") == ""
    assert camel_case("delete!") == "delete!"
    assert camel_case("HIGH FIVE!") == "highFive!"
    assert camel_case("A quick brown fox jumped over the lazy dog.") == "aQuickBrownFoxJumpedOverTheLazyDog"
    assert camel_case("tit-for-tat") == "titForTat"
    assert camel_case("words_seprated_by_underscores") == "wordsSepratedByUnderscores"
    assert camel_case("recursion.is.cool!") == "recursionIsCool!"
    assert camel_case("THIS%IS%A%PART%OF%A%LINK") == "thisIsAPartOfALink"