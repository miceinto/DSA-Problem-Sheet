import re

def is_palindrome(s):
    """
    Checks if the string is a palindrome after cleaning.
    
    Args:
    s (str): Input string
    
    Returns:
    bool: True if palindrome, False otherwise
    """
    # Clean the string: lowercase and remove non-alphanumeric
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check palindrome
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Time Complexity: O(n)
# Space Complexity: O(n) due to string cleaning
