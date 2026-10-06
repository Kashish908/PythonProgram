# Test_Code/test09_leap_year.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("leap_year", "Code/09_leap_year.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.is_leap_year(2020) == True
assert module.is_leap_year(2021) == False
assert module.is_leap_year(1900) == False
assert module.is_leap_year(2000) == True
assert module.is_leap_year(2024) == True

print("All test cases passed.")