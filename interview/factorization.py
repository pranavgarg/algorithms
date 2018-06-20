import timeit
def factors(n):
    if n == 2:
        return []
    factors = []
    p = 2
    while True:
        if n < p:
            return factors
        if n%p == 0:
            factors.append(p)
        p = p + 1

print factors(24)
assert factors(24) == [2,3,4,6,8,12,24]

timeit(factors)