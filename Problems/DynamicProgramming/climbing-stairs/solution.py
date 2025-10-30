def climb_stairs(n):
    """
    Calculates the number of ways to climb n stairs.
    
    Args:
    n (int): Number of stairs
    
    Returns:
    int: Number of distinct ways
    """
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)
# Can be optimized to O(1) space by keeping only last two values.
