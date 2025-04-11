class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def dfs(nums, path, ans):
            if not nums:
                ans.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], ans)

        dfs(nums, [], ans)
        return ans
        