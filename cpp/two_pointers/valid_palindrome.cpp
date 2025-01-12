#include <cstring>
class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> forward;
        vector<char> backward;
        for (int i = 0; i < s.length(); i++) {
            if (!isalnum(s[i])) {
                continue;
            } else {
                
                forward.push_back(tolower(s[i]));
            }
        }
        for (int i = s.length() - 1; i >= 0; i--) {
            if (!isalnum(s[i])) {
                continue;
            } else {
                backward.push_back(tolower(s[i]));
            }
        }
        for (int i = 0; i < forward.size(); i++) {
            if (forward[i] == backward[i]) {
                continue;
            } else {
                return false;
            }
        }
        return true;
    }
};