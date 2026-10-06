# Code/14_sum_digits.py
def sum_of_digits(n):
    # Use absolute value to handle negative numbers safely
    return sum(int(digit) for digit in str(abs(n)))