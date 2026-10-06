# Code/11_gcd.py
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)