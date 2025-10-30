def max_subarray(nums):
    """
    Finds the maximum subarray sum using Kadane's algorithm.
    
    Args:
    nums (List[int]): List of integers
    
    Returns:
    int: Maximum subarray sum
    """
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

# Time Complexity: O(n)
# Space Complexity: O(1)
