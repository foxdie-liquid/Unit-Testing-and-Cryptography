import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    new_str = ""
    for i in range(0, len(text)):
        ind = alpha.find(text[i])
        ind = (ind * a + b) % 26
        new_str += alpha[ind]
    return new_str

def affine_decode(text, a, b):
    new_str = ""
    for i in range(0, len(text)):
        ind = alpha.find(text[i])
        ind = (ind * b - a) % 26
        new_str += alpha[ind]
    return new_str

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    mung = 0
    for i in range(0, len(ngram)):
        ind = alpha.find(ngram[i])
        mung += ind * (26 ** i)
    return mung

def convert_to_text(num, n):
    new_str = ""
    for i in range(0, n):
        num_temp = num // 26
        remainder = num % 26
        new_str += alpha[remainder]
        num = num_temp
    return new_str


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    return ''

def affine_n_decode(text, n, a, b):
    return ''

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!