from string import ascii_lowercase, ascii_uppercase

def rotate(text, offset):
  new_lowercase = ascii_lowercase[offset:] + ascii_lowercase[:offset]
  new_uppercase = ascii_uppercase[offset:] + ascii_uppercase[:offset]
  translation = str.maketrans(ascii_lowercase + ascii_uppercase, new_lowercase + new_uppercase)
  return text.translate(translation)
