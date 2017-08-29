SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)

def check_lists(a, b):
  if a == b:
    return EQUAL
  elif is_sublist(b, a):
    return SUPERLIST
  elif is_sublist(a, b):
    return SUBLIST
  else:
    return UNEQUAL

def is_sublist(short, long):
  for i in range(len(long) - len(short) + 1):
    if long[i:i + len(short)] == short: return True
  return False
