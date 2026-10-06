import sys
import os
import importlib

# Ensures Python can locate the root directory properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically loads the module to bypass the number syntax error
fib_module = importlib.import_module("Code.05_fibonacci_series")
fibonacci = fib_module.fibonacci

def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(1) == [0]
    assert fibonacci(0) == []

if __name__ == "__main__":
    test_fibonacci()
    print("All test cases passed.")