class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans;
        int count = 0;
        for (int& num : nums) {
            if (!count) {
                ans = num;
            }
            count += (num == ans) ? 1 : -1;
        }
        return ans;
    }
};