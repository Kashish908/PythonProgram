# Test_Code/test19_binary_search.py
import importlib.util

spec = importlib.util.spec_from_file_location("binary_search", "Code/19_binary_search.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Note: Binary search requires a sorted list
assert module.binary_search([10, 20, 30, 40, 50], 40) == 3
assert module.binary_search([1, 3, 5, 7, 9], 2) == -1
assert module.binary_search([5], 5) == 0
assert module.binary_search([], 10) == -1

print("All test cases passed.")