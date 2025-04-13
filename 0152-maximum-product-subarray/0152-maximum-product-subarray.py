class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        curr_max = nums[0]
        curr_min = nums[0]

        ans = curr_max

        for i in range(1, len(nums)):
            curr = nums[i]

            temp_max = max(curr, max(curr_max * curr, curr_min * curr))
            curr_min = min(curr, min(curr_max * curr, curr_min * curr))
            curr_max = temp_max
            ans = max(ans, curr_max)

        return ans
        