class Solution {
public:
    unordered_map<int, int> memo;
    int climbStairs(int n) {
        if (!memo[n]) {
            if (n <= 2) {
                memo[n] = n;
            } else {
                memo[n] = climbStairs(n - 1) + climbStairs(n - 2);
            }
        }
        return memo[n];
    }
};