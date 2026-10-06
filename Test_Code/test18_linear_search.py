# Test_Code/test18_linear_search.py
import importlib.util

spec = importlib.util.spec_from_file_location("linear_search", "Code/18_linear_search.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.linear_search([10, 20, 30, 40], 30) == 2
assert module.linear_search([5, 3, 8, 2], 9) == -1
assert module.linear_search([1], 1) == 0
assert module.linear_search([], 5) == -1

print("All test cases passed.")