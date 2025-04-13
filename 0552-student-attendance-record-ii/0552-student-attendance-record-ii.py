class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for size in range(n):
            for i in range(2):
                for j in range(3):
                    dp[size + 1][i][0] = (dp[size + 1][i][0] + dp[size][i][j]) % MOD
                    if i < 1:
                        dp[size + 1][i + 1][0] = (dp[size + 1][i + 1][0] + dp[size][i][j]) % MOD
                    if j < 2:
                        dp[size + 1][i][j + 1] = (dp[size + 1][i][j + 1] + dp[size][i][j]) % MOD

        ans = 0
        for i in range(2):
            for j in range(3):
                ans = (ans + dp[n][i][j]) % MOD

        return ans

        