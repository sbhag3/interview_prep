class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        dp = [[0] * (2 * total + 1) for _ in range(n)]
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, n):
            for j in range(-total, total + 1):
                if dp[i - 1][j + total] > 0:
                    dp[i][j + nums[i] + total] += dp[i - 1][j + total]
                    dp[i][j - nums[i] + total] += dp[i - 1][j + total]

        return 0 if abs(target) > total else dp[n - 1][target + total]
        