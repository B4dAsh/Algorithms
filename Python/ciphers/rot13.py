from string import ascii_uppercase, ascii_lowercase

def rot13(before_text) -> str:
    """
        ROT13.
        Time complexity - O(52 * n) -> O(n) | Ω(n)
        Space complexity - O(n)

        A modification of Caesar Cipher where each alphabet is shifted 
        13 places which means the same algorithm can be used to encrypt as 
        well as decrypt the text. Just like caesar cipher, It is not very 
        secure and easy to break.
    """

    after_text = ""

    for i in range(len(before_text)): # Iterate over the text,

        char = before_text[i] # Store one char at a time.

        if char in ascii_uppercase: 
            # Shift it 13 places and append to end of after text.
            after_text += ascii_uppercase[(ascii_uppercase.index(char) - 13) % 26]
        elif char in ascii_lowercase:
            after_text += ascii_lowercase[(ascii_lowercase.index(char) - 13) % 26]
        else: # If char is not alphabet.
            after_text += char
    
    return after_text


if __name__ == "__main__":
    # Tests
    assert rot13("") == ""
    assert rot13("a") == "n"
    assert rot13(rot13("rot13")) == "rot13"
    assert rot13("Inyne Zbetuhyvf") == "Valar Morghulis"