def sieve(n):
  candidates = list(range(2, n + 1))
  primes = []
  while candidates:
    prime = candidates[0]
    candidates = [c for c in candidates if c % prime]
    primes.append(prime)

  return primes
