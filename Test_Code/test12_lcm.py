# Test_Code/test12_lcm.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("lcm", "Code/12_lcm.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.find_lcm(12, 18) == 36
assert module.find_lcm(5, 7) == 35
assert module.find_lcm(0, 10) == 0
assert module.find_lcm(8, 8) == 8
assert module.find_lcm(15, 20) == 60

print("All test cases passed.")