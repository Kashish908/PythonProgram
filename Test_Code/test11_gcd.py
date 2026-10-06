# Test_Code/test11_gcd.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("gcd", "Code/11_gcd.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.find_gcd(60, 48) == 12
assert module.find_gcd(8, 9) == 1
assert module.find_gcd(0, 5) == 5
assert module.find_gcd(13, 13) == 13
assert module.find_gcd(-4, 14) == 2

print("All test cases passed.")