def reverse_string(s):
    """
    Reverses the string in-place.
    
    Args:
    s (List[str]): List of characters
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Time Complexity: O(n)
# Space Complexity: O(1)
