def distance(s1, s2):
  if len(s1) != len(s2): raise ValueError
  return sum(x != y for x, y in zip(s1, s2))
