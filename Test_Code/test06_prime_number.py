import sys
import os
import importlib

# Ensures Python can locate the root directory properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically loads the module to bypass number syntax errors
prime_module = importlib.import_module("Code.06_prime_number")
is_prime = prime_module.is_prime

def test_is_prime():
    assert is_prime(11) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(2) is True

if __name__ == "__main__":
    test_is_prime()
    print("All test cases passed.")