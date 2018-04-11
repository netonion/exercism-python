def nth_prime(positive_number):
    if positive_number <= 0:
        raise ValueError("Must be greater than zero")

    primes = []
    candidate = 2
    while len(primes) < positive_number:
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            primes.append(candidate)

        candidate += 1

    return primes[-1]
