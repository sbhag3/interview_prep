class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()

        def dfs(nums, target, index, path, ans):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return
            for i in range(index, len(nums)):
                dfs(nums, target - nums[i], i, path + [nums[i]], ans)

        dfs(candidates, target, 0, [], ans)
        return ans
        