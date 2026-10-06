import os
import sys
import importlib

# Add the Code directory to the system path to prevent import errors
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))

# Load the module dynamically
module = importlib.import_module("19_find_duplicates")
find_duplicates = module.find_duplicates

def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 3, 5]) == [2, 3]
    assert find_duplicates(["a", "b", "c"]) == []
    assert find_duplicates([1, 1, 1, 1]) == [1]
    assert find_duplicates([]) == []

if __name__ == "__main__":
    test_find_duplicates()
    print("All test cases passed.")