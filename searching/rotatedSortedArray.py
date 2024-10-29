def search_rotated_sorted_array(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the mid element is the target
        if arr[mid] == target:
            return mid
        
        # Check which half is sorted
        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:  # Target is in the left half
                right = mid - 1
            else:  # Target is in the right half
                left = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:  # Target is in the right half
                left = mid + 1
            else:  # Target is in the left half
                right = mid - 1
    
    return -1  # Target not found

# Example usage:
arr = [13, 15, 17, 19, 1, 3, 5, 7, 9, 11]
target = 5
result = search_rotated_sorted_array(arr, target)
print(f"Element found at index {result}" if result != -1 else "Element not found")
