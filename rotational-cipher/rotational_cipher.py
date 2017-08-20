def rotate(text, offset):
  res = ''
  for t in text:
    if ord('a') <= ord(t) <= ord('z'):
      res += chr(ord('a') + (ord(t) + offset - ord('a')) % 26)
    elif ord('A') <= ord(t) <= ord('Z'):
      res += chr(ord('A') + (ord(t) + offset - ord('A')) % 26)
    else:
      res += t

  return res
