from functools import reduce
from operator import mul

def largest_product(text, n):
  if n < 0: raise ValueError
  return max(reduce(mul, [int(d) for d in text[i:i + n]], 1) for i in range(len(text) - n + 1))
