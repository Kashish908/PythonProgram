import sys
import os
import importlib

# Ensures Python can locate the root directory properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically loads the module to bypass the number syntax error
pal_module = importlib.import_module("Code.09_palindrome_number")
is_palindrome_num = pal_module.is_palindrome_num

def test_is_palindrome_num():
    assert is_palindrome_num(121) is True
    assert is_palindrome_num(123) is False
    assert is_palindrome_num(7) is True
    assert is_palindrome_num(11) is True

if __name__ == "__main__":
    test_is_palindrome_num()
    print("All test cases passed.")