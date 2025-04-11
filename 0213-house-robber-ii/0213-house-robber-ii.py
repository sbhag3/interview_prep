class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dp(nums):
            t1 = 0
            t2 = 0
            for num in nums:
                temp = t1
                t1 = max(num + t2, t1)
                t2 = temp
            return t1

        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(dp(nums[:-1]), dp(nums[1:]))
        
        