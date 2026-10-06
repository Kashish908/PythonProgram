# Test_Code/test05_prime.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("prime", "Code/05_prime.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.is_prime(2) == True
assert module.is_prime(4) == False
assert module.is_prime(11) == True
assert module.is_prime(1) == False
assert module.is_prime(-7) == False

print("All test cases passed.")