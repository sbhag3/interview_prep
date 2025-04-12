class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        delta = [(nums[i] ^ k) - nums[i] for i in range(n)]
        delta.sort(reverse=True)
        ans = sum(nums)

        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                break
            path_delta = delta[i] + delta[i + 1]
            if path_delta <= 0:
                break
            ans += path_delta

        return ans

        