# Test_Code/test10_calculator.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("calculator", "Code/10_calculator.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.calculate(10, 5, "+") == 15
assert module.calculate(10, 5, "-") == 5
assert module.calculate(10, 5, "*") == 50
assert module.calculate(10, 2, "/") == 5.0
assert module.calculate(10, 0, "/") == "Error: Division by zero"
assert module.calculate(10, 5, "%") == "Error: Invalid operation"

print("All test cases passed.")