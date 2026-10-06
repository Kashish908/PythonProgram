def find_duplicates(lst):
    """Return a list containing only the duplicate elements from the input list."""
    seen = []
    duplicates = []
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        elif item not in seen:
            seen.append(item)
    return duplicates

if __name__ == "__main__":
    elements = input("Enter elements separated by spaces: ")
    input_list = elements.split()
    print(f"Duplicate elements: {find_duplicates(input_list)}")