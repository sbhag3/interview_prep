class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr = nums[0];
        int max_ = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            curr = max(nums[i], curr + nums[i]);
            max_ = max(curr, max_);
        }
        return max_;
    }
};