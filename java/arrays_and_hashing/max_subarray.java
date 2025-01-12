class Solution {
    public int maxSubArray(int[] nums) {
        int curr = nums[0];
        int max_ = nums[0];
        for (int i = 1; i < nums.length; i++) {
            curr = Math.max(nums[i], curr + nums[i]);
            max_ = Math.max(curr, max_);
        }
        return max_;
    }
}