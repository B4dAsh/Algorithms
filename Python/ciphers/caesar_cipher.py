from string import ascii_uppercase, ascii_lowercase

def caesar_cipher(before_text, key=13) -> str:
    """
        Caesar Cipher.
        Time complexity - O(52 * n) -> O(n) | Ω(n)
        Space complexity - O(n)

        Caesar cipher is an ancient encryption algorithm where each character 
        in plain text is shifted "key" number of places. When decrypting 
        same algorithm can be used by changing the key using the formula:

        decryption_key = 26 - encryption_key.

        Obviously, this encryption provides no security whatsoever.
    """

    after_text = ""

    for i in range(len(before_text)): # Iterate over the text, 

        char = before_text[i] # Checking one character at a time 

        if char in ascii_uppercase:
            # Shift it "key" number of places and append to the end of after text.
            after_text += ascii_uppercase[(ascii_uppercase.index(char) + key) % 26]
        elif char in ascii_lowercase:
            after_text += ascii_lowercase[(ascii_lowercase.index(char) + key) % 26]
        else: # If char is not an alphabet.
            after_text += char

    return after_text


if __name__ == "__main__":
    # Tests
    # For decryption, key = 26 - encryption key.
    assert caesar_cipher("") == ""
    assert caesar_cipher("a", 1) == "b"
    assert caesar_cipher("z", 25) == "y"
    assert caesar_cipher(caesar_cipher("ROT13")) == "ROT13"
    assert caesar_cipher("Veni, Vidi, Vici", 10) == "Foxs, Fsns, Fsms"
