def sum_of_multiples(n, factors):
  return sum(x for x in range(n) if any(not x % f for f in factors))
