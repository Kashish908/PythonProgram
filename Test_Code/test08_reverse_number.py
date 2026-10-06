import sys
import os
import importlib

# Ensures Python can locate the root directory properly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Dynamically loads the module to bypass the number syntax error
rev_module = importlib.import_module("Code.08_reverse_number")
reverse_num = rev_module.reverse_num

def test_reverse_num():
    assert reverse_num(123) == 321
    assert reverse_num(-45) == -54
    assert reverse_num(120) == 21
    assert reverse_num(0) == 0

if __name__ == "__main__":
    test_reverse_num()
    print("All test cases passed.")