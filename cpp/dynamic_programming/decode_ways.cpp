class Solution {
public:
    int numDecodings(string s) {
        if (s[0] == '0') return 0;

        int n = s.size();
        int two = 1;
        int one = 1;

        for (int i = 1; i < n; i++) {
            int curr = 0;
            if (s[i] != '0') {
                curr = one;
            }
            int temp = stoi(s.substr(i - 1, 2));
            if (temp >= 10 && temp <= 26) {
                curr += two;
            }
            two = one;
            one = curr;
        }
        return one;
    }
};