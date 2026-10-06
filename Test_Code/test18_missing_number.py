import os
import sys
import importlib

# Add the Code directory to the system path to prevent import errors
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))

# Load the module dynamically
module = importlib.import_module("18_missing_number")
find_missing_number = module.find_missing_number

def test_missing_number():
    assert find_missing_number([1, 2, 4, 5], 5) == 3
    assert find_missing_number([2, 3, 4], 4) == 1
    assert find_missing_number([1, 2, 3], 4) == 4

if __name__ == "__main__":
    test_missing_number()
    print("All test cases passed.")