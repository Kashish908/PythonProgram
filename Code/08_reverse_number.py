def reverse_num(n):
    """Reverses the digits of an integer, maintaining its sign."""
    sign = -1 if n < 0 else 1
    reversed_str = str(abs(n))[::-1]
    return sign * int(reversed_str)

if __name__ == "__main__":
    # Example check
    print(reverse_num(-123))