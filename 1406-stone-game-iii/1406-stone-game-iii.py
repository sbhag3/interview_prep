class Solution(object):
    def stoneGameIII(self, s):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(s)

        dp = [0] * (n + 1)
        

        for i in range(n - 1, -1, -1):
            dp[i] = s[i] - dp[i + 1]
            if i + 2 <= n:
                dp[i] = max(dp[i], s[i] + s[i + 1] - dp[i + 2])
            
            if i + 3 <= n:
                dp[i] = max(dp[i], s[i] + s[i + 1] + s[i + 2] - dp[i + 3])

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"