class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = set()
        ans = 0
        trav = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                trav -= nums[left]
                seen.remove(nums[left])
                left += 1

            seen.add(nums[right])
            trav += nums[right]

            if (right - left + 1) == k:
                ans = max(ans, trav)
                trav -= nums[left]
                seen.remove(nums[left])
                left += 1

        return ans
        