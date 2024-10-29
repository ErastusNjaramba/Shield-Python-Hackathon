def regex_match(s, p):
    # Create a DP table with dimensions (len(s)+1) x (len(p)+1)
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty string and empty pattern are a match
    dp[0][0] = True
    
    # Handle patterns with '*' that match an empty string (zero occurrences of the preceding char)
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]  # '*' can match zero of the preceding char
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match or '.' matches any char
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # '*' matches zero occurrences of the previous char
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]  # '*' matches one or more of the preceding char
    
    return dp[len(s)][len(p)]

# Example usage:
s = "aab"
p = "c*a*b"
print(f"Does the pattern match? {regex_match(s, p)}")
