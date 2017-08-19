def distance(s1, s2):
  if len(s1) != len(s2):
    raise ValueError

  count = 0
  for i, x in enumerate(s1):
    if x != s2[i]:
      count += 1

  return count
