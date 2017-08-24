def flatten(arr):
  if not arr:
    return []
  if isinstance(arr[0], list):
    return flatten(arr[0]) + flatten(arr[1:])
  elif arr[0] or arr[0] == 0:
    return [arr[0]] + flatten(arr[1:])
  else:
    return flatten(arr[1:])
