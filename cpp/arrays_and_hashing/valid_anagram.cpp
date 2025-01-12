class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        vector<int> table(26, 0);
        for (int i = 0; i < s.length(); i++) {
            freq[s[i] - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            freq[t[i] - 'a']--;
            if (freq[t[i] - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};