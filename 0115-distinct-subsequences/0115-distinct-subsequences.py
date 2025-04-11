class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)

        dp = [0 for j in range(n)]

        for i in range(m - 1, -1, -1):
            prev = 1
            for j in range(n - 1, -1, -1):
                old = dp[j]
                if s[i] == t[j]:
                    dp[j] += prev
                prev = old

        return dp[0]
        