# Code/16_factors.py
def find_factors(n):
    if n <= 0:
        return []
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors