def primitive_triplets(b):
    if b % 4: raise ValueError
    b = b // 2
    results = set()
    for m in range(2, b + 1):
        n, mod = divmod(b, m)
        if not mod:
            coprime = all(n % f or m % f for f in range(2, min(m, n) + 1))
            if coprime: results.add(tuple(sorted([abs(n ** 2 - m ** 2), 2 * n * m, n ** 2 + m ** 2])))
    return results


def triplets_in_range(min, max):
    return set((i, j, k) for i in range(min, max + 1)
                          for j in range(i + 1, max + 1)
                          for k in range(j + 1, max + 1)
                          if is_triplet((i, j, k)))


def is_triplet(triplets):
    a, b, c = sorted(triplets)
    return a ** 2 + b ** 2 == c ** 2
