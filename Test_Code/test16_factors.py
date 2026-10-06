# Test_Code/test16_factors.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("factors", "Code/16_factors.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.find_factors(6) == [1, 2, 3, 6]
assert module.find_factors(1) == [1]
assert module.find_factors(7) == [1, 7]
assert module.find_factors(12) == [1, 2, 3, 4, 6, 12]
assert module.find_factors(0) == []

print("All test cases passed.")