# Test_Code/test17_bubble_sort.py
import importlib.util

# Dynamically load the module
spec = importlib.util.spec_from_file_location("bubble_sort", "Code/17_bubble_sort.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Test cases using assert
assert module.bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
assert module.bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
assert module.bubble_sort([]) == []
assert module.bubble_sort([1]) == [1]
assert module.bubble_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]

print("All test cases passed.")