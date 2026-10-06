# Test_Code/test14_sum_digits.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("sum_digits", "Code/14_sum_digits.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.sum_of_digits(123) == 6      # 1 + 2 + 3 = 6
assert module.sum_of_digits(4502) == 11    # 4 + 5 + 0 + 2 = 11
assert module.sum_of_digits(0) == 0       # 0 = 0
assert module.sum_of_digits(-98) == 17     # 9 + 8 = 17
assert module.sum_of_digits(7) == 7        # 7 = 7

print("All test cases passed.")