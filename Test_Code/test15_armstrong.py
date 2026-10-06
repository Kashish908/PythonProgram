# Test_Code/test15_armstrong.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("armstrong", "Code/15_armstrong.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.is_armstrong(153) == True   # 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
assert module.is_armstrong(9474) == True  # 9^4 + 4^4 + 7^4 + 4^4 = 9474
assert module.is_armstrong(0) == True     # 0^1 = 0
assert module.is_armstrong(123) == False
assert module.is_armstrong(-153) == False

print("All test cases passed.")