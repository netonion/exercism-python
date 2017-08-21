from string import ascii_lowercase, punctuation, whitespace

translation = str.maketrans(ascii_lowercase, ascii_lowercase[::-1], punctuation + whitespace)

def encode(msg):
  enc = msg.lower().translate(translation)
  return ' '.join([enc[i:i+5] for i in range(0, len(enc), 5)])

def decode(msg):
  return msg.translate(translation)
