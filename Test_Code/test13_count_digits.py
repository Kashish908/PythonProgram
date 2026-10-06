# Test_Code/test13_count_digits.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("count_digits", "Code/13_count_digits.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.count_digits(12345) == 5
assert module.count_digits(0) == 1
assert module.count_digits(-987) == 3
assert module.count_digits(7) == 1
assert module.count_digits(1000000) == 7

print("All test cases passed.")