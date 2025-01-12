class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int ans = 0;
        
        while (left < right) {
            int curr = min(height[left], height[right]) * (right - left);
            if (curr > ans) {
                ans = curr;
            } else {
                if (height[left] < height[right]) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return ans;
    }
};