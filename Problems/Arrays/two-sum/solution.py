def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    
    Args:
    nums (List[int]): List of integers
    target (int): Target sum
    
    Returns:
    List[int]: Indices of the two numbers
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # No solution found, though problem guarantees one

# Time Complexity: O(n)
# Space Complexity: O(n)
