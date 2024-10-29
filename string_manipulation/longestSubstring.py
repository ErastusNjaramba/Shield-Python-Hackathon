def longest_substring_without_repeating(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # If the character at the right pointer is already in the set, remove from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the current character to the set and update max_len
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Example usage:
s = "abcabcbb"
print(f"Length of the longest substring: {longest_substring_without_repeating(s)}")
