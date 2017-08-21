def translate(char):
  if char.isalpha():
    return chr(ord('z') - (ord(char) - ord('a')))
  elif char.isdigit():
    return char
  else:
    return ''

def encode(msg):
  res = ''
  for c in msg.lower():
    if len(res) % 6 == 5:
      res += ' '
    res += translate(c)

  return res.rstrip()

def decode(msg):
  return ''.join([translate(c) for c in msg])
