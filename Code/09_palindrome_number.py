def is_palindrome_num(n):
    """Checks if a number reads the same backward as forward."""
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    # Example check
    print(is_palindrome_num(121))