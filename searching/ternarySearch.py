def ternary_search(arr, left, right, key):
    if right >= left:

#         Example Walkthrough
# Suppose left = 0 and right = 9 for a list of 10 elements.

# mid1 = 0 + (9 - 0) // 3 = 0 + 3 = 3
# mid2 = 9 - (9 - 0) // 3 = 9 - 3 = 6
        # Divide the array into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Check if the key is present at mid1 or mid2

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        
        # Narrow down the search space
        if key < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, key)  # Search in the left third
        elif key > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, key)  # Search in the right third
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, key)  # Search in the middle third
    return -1  # Key not found


arr = [1, 12, 5, 7, 24, 11, 13, 6, 17, 19]
key = 2
result = ternary_search(arr, 0, len(arr) - 1, key)
print(f"Element found at index {result}" if result != -1 else "Element not found")
