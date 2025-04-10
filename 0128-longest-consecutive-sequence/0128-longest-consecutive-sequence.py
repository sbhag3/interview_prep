class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_set = set(nums)

        ans = 1

        for num in nums_set:
            streak = 1
            if num - 1 not in nums_set:
                x = num
                while x + 1 in nums_set:
                    streak += 1
                    x += 1
                ans = max(ans, streak)

        return ans
        