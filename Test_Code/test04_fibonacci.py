# Test_Code/test04_fibonacci.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("fibonacci", "Code/04_fibonacci.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.generate_fibonacci(0) == []
assert module.generate_fibonacci(1) == [0]
assert module.generate_fibonacci(2) == [0, 1]
assert module.generate_fibonacci(5) == [0, 1, 1, 2, 3]
assert module.generate_fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]

print("All test cases passed.")