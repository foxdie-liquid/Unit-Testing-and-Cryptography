# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def sub_encode(text, codebet):
    """
    converts text to an encoded string using codebet
    :param text: is the text to be encoded
    :param codebet: is the cipher alphabet
    :return: returns the encoded string
    """
    new_str = ""
    for let in text:
        index_alpha = alpha.find(let)
        new_str += codebet[index_alpha]
    return new_str


def sub_decode(text, codebet):
    """
    converts text to a decoded string using codebet
    :param text: is the returned string from sub_encode
    :param codebet: is the cipher alphabet
    :return: returns the original text
    """
    new_str = ""
    for let in text:
        index_cipher = codebet.find(let)
        new_str += alpha[index_cipher]
    return new_str


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
