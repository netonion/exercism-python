def flatten(arr):
  res = []
  for x in arr:
    if isinstance(x, list) or isinstance(x, tuple):
      res.extend(flatten(x))
    elif x is not None:
      res.append(x)
  return res
