package DSA-Problem-Sheet.Problems.Arrays.Maximum_Average_Subarray_1;

class Solution {
    /**
     * Finds the maximum average of any contiguous subarray of length k.
     *
     * @param nums Integer array of length n.
     * @param k Length of the subarray.
     * @return Maximum average value of any contiguous subarray of length k.
     */
    public double findMaxAverage(int[] nums, int k) {
        // Initialize the sum of the first window of size k
        double windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        // Initialize maximum sum as the sum of the first window
        double maxSum = windowSum;

        // Slide the window through the array
        for (int i = k; i < nums.length; i++) {
            // Update the window sum: add the next element, remove the first element of previous window
            windowSum = windowSum + nums[i] - nums[i - k];

            // Update the maximum sum if current window sum is larger
            maxSum = Math.max(maxSum, windowSum);
        }

        // Return the maximum average
        return maxSum / k;
    }
}
