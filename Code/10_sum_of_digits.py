def sum_digits(n):
    """Calculates the sum of the digits of a given integer."""
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == "__main__":
    # Example check
    print(sum_digits(123))