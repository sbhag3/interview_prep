class Solution {
public:
    string check(int left, int right, string temp) {
        while (left >= 0 && right < temp.size() && temp[left] == temp[right]) {
            left--;
            right++;
        }
        return temp.substr(left + 1, right - left - 1);
    }

    string longestPalindrome(string s) {
        string ans = "";
        for (int i = 0; i < s.size(); i++) {
            string one = check(i, i, s);
            if (one.size() > ans.size()) ans = one;
            string two = check(i, i+1, s);
            if (two.size() > ans.size()) ans = two;
        }
        return ans;

    }
};