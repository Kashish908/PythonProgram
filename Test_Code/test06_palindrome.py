# Test_Code/test06_palindrome.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("palindrome", "Code/06_palindrome.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.is_palindrome("radar") == True
assert module.is_palindrome("hello") == False
assert module.is_palindrome(121) == True
assert module.is_palindrome(123) == False
assert module.is_palindrome("A man a plan a canal Panama") == True

print("All test cases passed.")