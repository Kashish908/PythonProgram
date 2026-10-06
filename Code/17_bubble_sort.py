# Code/17_bubble_sort.py
def bubble_sort(arr):
    # Make a copy of the list to avoid modifying the original list directly
    sorted_arr = list(arr)
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap elements
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    return sorted_arr