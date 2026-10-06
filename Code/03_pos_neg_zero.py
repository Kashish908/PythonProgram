def check_number(num):
    """Checks if a number is positive, negative, or zero."""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == "__main__":
    # Example test
    print(check_number(10))