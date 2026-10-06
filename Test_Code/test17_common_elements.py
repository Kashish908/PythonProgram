import os
import sys
import importlib

# Add the Code directory to the system path to prevent import errors
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))

# Load the module dynamically
module = importlib.import_module("17_common_elements")
find_common_elements = module.find_common_elements

def test_common_elements():
    assert find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert find_common_elements(["a", "b"], ["c", "d"]) == []
    assert find_common_elements([1, 1, 2], [1, 3]) == [1]
    assert find_common_elements([], [1, 2]) == []

if __name__ == "__main__":
    test_common_elements()
    print("All test cases passed.")