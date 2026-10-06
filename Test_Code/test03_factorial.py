# Test_Code/test_03_factorial.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("factorial", "Code/03_factorial.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.factorial(0) == 1
assert module.factorial(1) == 1
assert module.factorial(5) == 120
assert module.factorial(3) == 6
assert module.factorial(-5) == None

print("All test cases passed.")