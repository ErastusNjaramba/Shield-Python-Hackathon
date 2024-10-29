import heapq

def kth_largest(nums, k):
    # Create a min-heap of the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Process the rest of the elements
    for num in nums[k:]:
        if num > min_heap[0]:  # Only add if the element is larger than the min in the heap
            heapq.heappushpop(min_heap, num)
    
    # The root of the heap is the Kth largest element
    return min_heap[0]

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"The {k}th largest element is: {kth_largest(nums, k)}")
