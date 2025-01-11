class Solution {
public:
    int findMin(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        int start = 0, end = nums.size() - 1;
        if (nums[end] > nums[0]) {
            return nums[0];
        }
        while (end >= start) {
            int middle = start + (end - start) / 2;
            if (nums[middle] > nums[middle + 1]) {
                return nums[middle + 1];
            }
            if (nums[middle - 1] > nums[middle]) {
                return nums[middle];
            }
            if (nums[middle] > nums[0]) {
                start = middle + 1;
            } else end = middle - 1;
        }
        return INT_MAX;
    }  
};