class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n

        ans[0] = 1
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]

        trav = 1
        for i in reversed(range(n)):
            ans[i] *= trav
            trav *= nums[i]
        return ans
        