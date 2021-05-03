from string import ascii_uppercase, ascii_lowercase

def caesar_cipher(before_text, key=13) -> str:
    """
        Caesar Cipher.
        Time complexity - O(52 * n) -> O(n) | Ω(n)
        Space complexity - O(n)

        Caesar cipher is a weak encryption algorithm where each character
        in plain text is shifted "key" number of places. When decrypting 
        same algorithm can be used by changing the key using following 
        formula:

        decryption_key = 26 - encryption_key.
    """

    after_text = ""

    for i in range(len(before_text)): # Iterate over the text,
        
        char = before_text[i] # Check one char at a time

        if char in ascii_uppercase:
            # Shift it "key" number of places and append to the end of after text.
            after_text += ascii_uppercase[(ascii_uppercase.index(char) + key) % 26]
        elif char in ascii_lowercase:
            after_text += ascii_lowercase[(ascii_lowercase.index(char) + key) % 26]
        else: # If char is not a alphabet.
            after_text += char

    return after_text


if __name__ == "__main__":
    # Tests
    # If decrypting, key = 26 - encrypting key.
    assert caesar_cipher("") == ""
    assert caesar_cipher("a", 1) == "b"
    assert caesar_cipher("z", 25) == "y"
    assert caesar_cipher(caesar_cipher("ROT13")) == "ROT13"
    assert caesar_cipher("Xtca Ctbzi", 18) == "Plus Ultra"