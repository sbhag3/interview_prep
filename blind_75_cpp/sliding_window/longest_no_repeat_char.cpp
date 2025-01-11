class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int maxLen = 0;
        vector<int> char_idx(128, -1);
        int left = 0;
        
        for (int right = 0; right < n; right++) {
            if (char_idx[s[right]] >= left) {
                left = char_idx[s[right]] + 1;
            }
            char_idx[s[right]] = right;
            maxLen = max(maxLen, right - left + 1);
        }
        return maxLen;
    }
};