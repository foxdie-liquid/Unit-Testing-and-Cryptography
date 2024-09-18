# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

def vig_encode(text, keyword):
  new_str = ""
  for i in range(len(text)):
    ind = alpha.find(text[i]) + alpha.find(keyword[i % len(keyword)])
    ind = ind % 27
    new_str += alpha[ind]
  return new_str




def vig_decode(text, keyword):
  new_str = ""
  for i in range(len(text)):
    ind = alpha.find(text[i]) - alpha.find(keyword[i % len(keyword)])
    ind = ind % 27
    new_str += alpha[ind]
  return new_str


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!