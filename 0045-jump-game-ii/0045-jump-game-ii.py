class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, n = 0, len(nums)
        end, farthest = 0, 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                ans += 1
                end = farthest

        return ans