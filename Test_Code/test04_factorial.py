import sys
import os
import importlib

# Ensures Python can locate the root directory properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically loads the module to bypass the number syntax error
factorial_module = importlib.import_module("Code.04_factorial")
factorial = factorial_module.factorial

def test_factorial():
    # Test cases matching factorial logic
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(-5) is None

if __name__ == "__main__":
    test_factorial()
    print("All test cases passed.")