#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxCurrent = nums[0], maxGlobal = nums[0];
        for (size_t i = 1; i < nums.size(); ++i) {
            maxCurrent = max(nums[i], maxCurrent + nums[i]);
            if (maxCurrent > maxGlobal) {
                maxGlobal = maxCurrent;
            }
        }
        return maxGlobal;
    }
};
