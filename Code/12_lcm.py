# Code/12_lcm.py
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // find_gcd(a, b)