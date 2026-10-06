import sys
import os
import importlib

# Ensures Python can locate the root directory properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically loads the module to bypass the number syntax error
pos_neg_module = importlib.import_module("Code.03_pos_neg_zero")
check_number = pos_neg_module.check_number

def test_check_number():
    # Test cases matching the logical choices
    assert check_number(10) == "Positive"
    assert check_number(-5) == "Negative"
    assert check_number(0) == "Zero"
    assert check_number(100) == "Positive"
    assert check_number(-100) == "Negative"

if __name__ == "__main__":
    test_check_number()
    print("All test cases passed.")