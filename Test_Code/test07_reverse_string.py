# Test_Code/test07_reverse_string.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("reverse_string", "Code/07_reverse_string.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.reverse_string("hello") == "olleh"
assert module.reverse_string("Python") == "nohtyP"
assert module.reverse_string("") == ""
assert module.reverse_string("a") == "a"
assert module.reverse_string("racecar") == "racecar"

print("All test cases passed.")