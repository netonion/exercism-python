def prime_factors(n):
  factors = []
  prime = 2
  while n > 1:
    while not n % prime:
      factors.append(prime)
      n /= prime
    prime += 1
  return factors
