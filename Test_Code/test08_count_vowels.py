# Test_Code/test08_count_vowels.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("count_vowels", "Code/08_count_vowels.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.count_vowels("hello") == 2
assert module.count_vowels("Python") == 1
assert module.count_vowels("AEIOU") == 5
assert module.count_vowels("xyz") == 0
assert module.count_vowels("") == 0

print("All test cases passed.")