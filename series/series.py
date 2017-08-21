def slices(text, n):
  if len(text) < n or not n: raise ValueError
  return [[int(d) for d in text[i:i + n]] for i in range(len(text) - n + 1)]
