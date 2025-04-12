class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []

        nums.sort()

        dp = [0] * n

        for i in range(n):
            size = 0
            for k in range(i):
                if nums[i] % nums[k] == 0:
                    size = max(size, dp[k])
            size += 1
            dp[i] = size

        maxSize, idx = max([(v, i) for i, v in enumerate(dp)])
        ans = []

        curr, end = maxSize, nums[idx]
        for i in range(idx, -1, -1):
            if curr == dp[i] and end % nums[i] == 0:
                ans.append(nums[i])
                curr -= 1
                end = nums[i]

        return ans
        