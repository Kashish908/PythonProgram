def find_common_elements(list1, list2):
    """Return a list containing elements that are present in both lists without duplicates."""
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

if __name__ == "__main__":
    lst1 = input("Enter first list elements separated by spaces: ").split()
    lst2 = input("Enter second list elements separated by spaces: ").split()
    print(f"Common elements: {find_common_elements(lst1, lst2)}")