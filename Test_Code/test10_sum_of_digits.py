import sys
import os
import importlib

# Ensures Python can locate the root directory properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically loads the module to bypass number syntax errors
sum_module = importlib.import_module("Code.10_sum_of_digits")
sum_digits = sum_module.sum_digits

def test_sum_digits():
    assert sum_digits(123) == 6
    assert sum_digits(505) == 10
    assert sum_digits(0) == 0
    assert sum_digits(-45) == 9

if __name__ == "__main__":
    test_sum_digits()
    print("All test cases passed.")