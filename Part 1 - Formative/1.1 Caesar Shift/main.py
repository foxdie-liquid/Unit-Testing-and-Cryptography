# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    """
    encodes a string using Caesar Cipher.
    :param text: is the text to be encrypted
    :param n: is the shift value
    :return: returns a new text in the form of encrypted text
    """
    new_str = ""
    for let in text:
        index = alpha.find(let)
        new_str += alpha[(index + n) % 26]
    return new_str


def caesar_decode(text, n):
    """
    decodes a string using Caesar Cipher.
    :param text: is the encrypted text to be decrypted
    :param n: is the shift value
    :return: returns a new text in the form of decrypted text
    """
    new_str = ""
    for let in text:
        index = alpha.find(let)
        new_str += alpha[(index - n) % 26]
    return new_str


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
