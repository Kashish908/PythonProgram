# Code/13_count_digits.py
def count_digits(n):
    # Use absolute value to handle negative numbers correctly
    return len(str(abs(n)))