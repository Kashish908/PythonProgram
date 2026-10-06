# Test_Code/test_02_largest_of_three.py
import importlib.util

# Dynamically load the module because the filename starts with a number
spec = importlib.util.spec_from_file_location(
    "largest_of_three", "Code/02_largest_of_three.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.find_largest(1, 5, 3) == 5
assert module.find_largest(10, 2, 4) == 10
assert module.find_largest(3, 3, 9) == 9
assert module.find_largest(-1, -5, -3) == -1
assert module.find_largest(7, 7, 7) == 7

print("All test cases passed.")
