# Code/06_palindrome.py
def is_palindrome(value):
    # Convert input to string, remove spaces, and convert to lowercase
    s = str(value).replace(" ", "").lower()
    return s == s[::-1]