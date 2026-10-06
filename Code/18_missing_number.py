def find_missing_number(numbers, n):
    """Return the missing number from a sequence of 1 to n."""
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

if __name__ == "__main__":
    n_val = int(input("Enter the total number of elements (n): "))
    elements = input(f"Enter elements from 1 to {n_val} with one missing, separated by spaces: ")
    num_list = [int(x) for x in elements.split()]
    print(f"Missing number: {find_missing_number(num_list, n_val)}")